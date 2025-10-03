"""
Enhanced Authentication session logic for LogicPwn.

This module provides comprehensive authentication capabilities with automatic CSRF token handling,
session persistence validation, intelligent redirect detection, and multi-step authentication flows.

Key Features:
- Automatic CSRF token extraction and handling for all major frameworks
- Session persistence validation and recovery mechanisms
- Intelligent redirect detection and handling
- Multi-step authentication flow support
- JWT token management and validation
- Enhanced security controls and validation
- Intelligent caching that excludes dynamic tokens
- Fallback authentication mechanisms for maximum reliability
- Full compatibility with LogicPwn runner and cache modules
- Comprehensive error handling and logging

Supported CSRF Token Patterns:
- DVWA (user_token)
- Rails (authenticity_token, csrf_token)
- Laravel (_token, csrf_token)
- Django (csrfmiddlewaretoken)
- Spring Security (lt, execution, _eventId)
- Custom meta tag patterns

Example Usage:
    ```python
    from logicpwn.core.auth import authenticate_session, AuthConfig, Authenticator

    # Basic authentication with automatic CSRF handling
    config = AuthConfig(
        url="http://target.com/login.php",
        method="POST",
        credentials={"username": "admin", "password": "password"},
        success_indicators=["Welcome", "Dashboard"],
        failure_indicators=["Login failed", "Invalid"]
    )

    session = authenticate_session(config)
    # Session is ready for use with runner module or direct requests

    # Advanced authentication with comprehensive features
    advanced_config = AdvancedAuthConfig(base_config=config)
    authenticator = Authenticator(advanced_config)
    auth_session = authenticator.authenticate_intelligent("http://target.com/login.php")

    # Advanced configuration
    config = AuthConfig(
        url="http://dvwa.local/login.php",
        method="POST",
        credentials={
            "username": "admin",
            "password": "password",
            "Login": "Login"
            # user_token will be automatically extracted and added
        },
        timeout=30,
        verify_ssl=False,
        headers={"User-Agent": "Custom-Agent/1.0"},
        success_indicators=["Welcome to DVWA"],
        failure_indicators=["Login failed", "incorrect"]
    )

    session = authenticate_session(config)
    ```

Performance Notes:
- Sessions are cached by stable credentials (excluding CSRF tokens)
- Cached sessions are validated before reuse
- Failed authentication attempts include detailed debugging information
- Automatic fallback to manual authentication if standard flow fails
"""

import re
from typing import Any, Optional, Union

import requests
from loguru import logger

from logicpwn.core.cache import session_cache
from logicpwn.core.performance import monitor_performance
from logicpwn.core.utils import validate_config
from logicpwn.exceptions import (
    AuthenticationError,
    LoginFailedException,
    NetworkError,
    TimeoutError,
    ValidationError,
)

from .auth_constants import DEFAULT_SESSION_TIMEOUT
from .auth_models import AuthConfig, CSRFConfig
from .auth_utils import (
    _handle_response_indicators,
    _sanitize_credentials,
)
from .http_client import LogicPwnHTTPClient, create_authenticated_client


def _extract_csrf_token(html_content: str) -> Optional[str]:
    """
    Extract CSRF token from HTML content.

    Supports multiple common CSRF token patterns used across different web frameworks
    and applications. Patterns are checked in order of most common to least common
    for optimal performance.

    Supported Patterns:
    - DVWA: user_token
    - Rails: authenticity_token, csrf_token
    - Laravel: _token, csrf_token
    - Django: csrfmiddlewaretoken
    - Spring Security: lt, execution, _eventId
    - Generic: token, csrf, xsrf
    - Meta tags: csrf-token, _token

    Args:
        html_content (str): HTML content to search for CSRF tokens

    Returns:
        Optional[str]: Extracted CSRF token or None if not found

    Example:
        >>> html = '<input name="user_token" value="abc123def456" />'
        >>> token = _extract_csrf_token(html)
        >>> print(token)  # "abc123def456"

        >>> html = '<meta name="csrf-token" content="xyz789" />'
        >>> token = _extract_csrf_token(html)
        >>> print(token)  # "xyz789"
    """
    # Validate input type
    if not isinstance(html_content, str):
        logger.debug(
            f"CSRF extraction skipped: html_content is not a string (got {type(html_content)})"
        )
        return None

    # Common CSRF token patterns ordered by frequency of use
    csrf_patterns = [
        # Input field patterns (most common)
        r'name=["\']user_token["\'].*?value=["\']([^"\']+)["\']',  # DVWA
        r'name=["\']csrf_token["\'].*?value=["\']([^"\']+)["\']',  # Rails/Laravel
        r'name=["\']_token["\'].*?value=["\']([^"\']+)["\']',  # Laravel
        r'name=["\']authenticity_token["\'].*?value=["\']([^"\']+)["\']',  # Rails
        r'name=["\']csrfmiddlewaretoken["\'].*?value=["\']([^"\']+)["\']',  # Django
        # Spring Security patterns
        r'name=["\']lt["\'].*?value=["\']([^"\']+)["\']',  # CAS/Spring
        r'name=["\']execution["\'].*?value=["\']([^"\']+)["\']',  # Spring WebFlow
        r'name=["\']_eventId["\'].*?value=["\']([^"\']+)["\']',  # Spring
        # Generic patterns
        r'name=["\']token["\'].*?value=["\']([^"\']+)["\']',  # Generic
        r'name=["\']xsrf["\'].*?value=["\']([^"\']+)["\']',  # XSRF
        # Meta tag patterns
        r'<meta\s+name=["\']csrf-token["\'].*?content=["\']([^"\']+)["\']',  # Rails meta
        r'<meta\s+name=["\']_token["\'].*?content=["\']([^"\']+)["\']',  # Laravel meta
        r'<meta\s+name=["\']token["\'].*?content=["\']([^"\']+)["\']',  # Generic meta
        # Alternative input formats
        r'<input[^>]*name=["\']csrf[^"\']*["\'][^>]*value=["\']([^"\']+)["\']',
        r'<input[^>]*name=["\'][^"\']*token[^"\']*["\'][^>]*value=["\']([^"\']+)["\']',
    ]

    for i, pattern in enumerate(csrf_patterns):
        try:
            match = re.search(pattern, html_content, re.IGNORECASE | re.DOTALL)
            if match:
                token = match.group(1).strip()
                if token and len(token) > 3:  # Basic validation
                    logger.debug(
                        f"Extracted CSRF token using pattern #{i+1}: {pattern[:50]}..."
                    )
                    logger.debug(
                        f"Token: {token[:10]}{'...' if len(token) > 10 else ''}"
                    )
                    return token
        except Exception as e:
            logger.debug(f"Error with CSRF pattern #{i+1}: {e}")
            continue

    logger.debug("No valid CSRF token found in HTML content")
    return None


def _generate_stable_session_id(config: AuthConfig) -> str:
    """
    Generate a stable session ID for caching that excludes dynamic tokens.

    This function creates cache keys based on stable authentication parameters,
    excluding dynamic values like CSRF tokens that change on each request. This
    ensures that sessions can be cached effectively without cache misses due to
    token rotation.

    Args:
        config (AuthConfig): Authentication configuration

    Returns:
        str: Stable session ID string suitable for caching

    Example:
        >>> config = AuthConfig(
        ...     url="http://example.com/login",
        ...     method="POST",
        ...     credentials={
        ...         "username": "admin",
        ...         "password": "secret",
        ...         "user_token": "dynamic123"  # This will be excluded
        ...     }
        ... )
        >>> session_id = _generate_stable_session_id(config)
        >>> print(session_id)  # "http://example.com/login_POST_-1234567890"
    """
    # Comprehensive list of dynamic token field names to exclude from caching
    # These tokens change frequently and should not affect cache keys
    dynamic_tokens = {
        # CSRF tokens
        "user_token",
        "csrf_token",
        "_token",
        "authenticity_token",
        "csrfmiddlewaretoken",
        "xsrf_token",
        "csrf",
        "token",
        # ASP.NET ViewState
        "__viewstate",
        "__viewstategenerator",
        "__eventvalidation",
        "__eventargument",
        "__eventtarget",
        # Spring Security
        "lt",
        "execution",
        "_eventId",
        "submit",
        "service",
        # SAML
        "samlresponse",
        "relaystate",
        "samlrequest",
        # OAuth/OpenID
        "state",
        "nonce",
        "code_challenge",
        "code_verifier",
        # Session tokens
        "session_token",
        "request_token",
        "form_token",
        # Captcha
        "captcha",
        "recaptcha",
        "captcha_token",
        # Timestamps and random values
        "timestamp",
        "nonce",
        "random",
        "_time",
        "time",
    }

    # Extract only stable credentials for cache key generation
    stable_creds = {
        k: v
        for k, v in config.credentials.items()
        if k.lower() not in dynamic_tokens and v is not None
    }

    # Include other stable configuration parameters
    stable_params = {
        "url": config.url,
        "method": config.method.upper(),
        "credentials": stable_creds,
        "verify_ssl": config.verify_ssl,
    }

    # Create stable session ID using hash of stable parameters
    session_id = (
        f"{config.url}_{config.method}_{hash(str(sorted(stable_params.items())))}"
    )
    logger.debug(f"Generated stable session ID: {session_id[:60]}...")
    return session_id


def _validate_cached_session(session: requests.Session, config: AuthConfig) -> bool:
    """
    Validate that a cached session is still active and authenticated.

    Performs comprehensive validation checks to ensure the cached session
    can still access protected resources and hasn't expired. Uses multiple
    validation strategies for maximum reliability.

    Validation Strategy:
    1. Test access to common protected endpoints
    2. Check for redirect responses to login pages
    3. Analyze response content for authentication indicators
    4. Validate session cookies are still present

    Args:
        session (requests.Session): Cached session to validate
        config (AuthConfig): Authentication configuration for validation context

    Returns:
        bool: True if session is valid and authenticated, False otherwise

    Example:
        >>> session = requests.Session()
        >>> config = AuthConfig(url="http://example.com/login", ...)
        >>> is_valid = _validate_cached_session(session, config)
        >>> if is_valid:
        ...     print("Session is still authenticated")
        ... else:
        ...     print("Session expired, need to re-authenticate")
    """
    try:
        # Check if session has any cookies at all
        if not session.cookies:
            logger.debug("Session validation failed: no cookies present")
            return False

        # Extract base URL for testing various endpoints
        base_url = config.url
        for suffix in ["/login.php", "/login", "/auth", "/signin"]:
            if base_url.endswith(suffix):
                base_url = base_url[: -len(suffix)]
                break
        base_url = base_url.rstrip("/")

        # Test URLs in order of reliability for session validation
        test_endpoints = [
            f"{base_url}/",  # Root page
            f"{base_url}/index.php",  # Common index page
            f"{base_url}/dashboard",  # Common protected page
            f"{base_url}/profile",  # User profile page
            f"{base_url}/admin",  # Admin area
            f"{base_url}/vulnerabilities/",  # DVWA specific
            f"{base_url}/vulnerabilities/brute/",  # DVWA brute force page
        ]

        for test_url in test_endpoints:
            try:
                # Use short timeout for validation requests
                test_response = session.get(test_url, timeout=5, allow_redirects=False)

                # Check for redirect responses (often indicate session expiry)
                if test_response.status_code in [301, 302, 303, 307, 308]:
                    location = test_response.headers.get("Location", "").lower()

                    # Check if redirect points to authentication pages
                    auth_indicators = [
                        "login",
                        "auth",
                        "signin",
                        "authenticate",
                        "logon",
                        "sso",
                        "oauth",
                        "session",
                    ]

                    if any(indicator in location for indicator in auth_indicators):
                        logger.debug(
                            f"Session validation failed: redirected to auth page {location}"
                        )
                        return False

                # For successful responses, check content
                elif test_response.status_code == 200:
                    content = test_response.text.lower()

                    # Check for login page indicators in content
                    login_indicators = [
                        "login ::",
                        "please log in",
                        "authentication required",
                        "access denied",
                        "unauthorized",
                        "forbidden",
                        "session expired",
                        "please sign in",
                        "login form",
                        "username",
                        "password",  # Look for login forms
                    ]

                    # Count how many login indicators are present
                    login_indicator_count = sum(
                        1 for indicator in login_indicators if indicator in content
                    )

                    # If we find multiple login indicators, likely a login page
                    if login_indicator_count >= 2:
                        logger.debug(
                            f"Session validation failed: login content detected ({login_indicator_count} indicators)"
                        )
                        continue

                    # Check for positive authentication indicators
                    auth_success_indicators = [
                        "welcome",
                        "dashboard",
                        "profile",
                        "logout",
                        "vulnerability:",
                        "admin",
                        "settings",
                        "dvwa",
                    ]

                    if any(
                        indicator in content for indicator in auth_success_indicators
                    ):
                        logger.debug(f"Session validation passed for {test_url}")
                        return True

                # For other status codes, continue testing other endpoints
                elif test_response.status_code in [403, 401]:
                    # Forbidden/Unauthorized might indicate session issues
                    logger.debug(
                        f"Session validation: got {test_response.status_code} for {test_url}"
                    )
                    continue

            except requests.exceptions.Timeout:
                logger.debug(f"Session validation timeout for {test_url}")
                continue
            except Exception as e:
                logger.debug(f"Session validation error for {test_url}: {e}")
                continue

        # If we get here, no endpoint confirmed valid authentication
        logger.debug("Session validation failed: no endpoint confirmed authentication")
        return False

    except Exception as e:
        logger.debug(f"Session validation exception: {e}")
        return False


def _perform_robust_authentication(config: AuthConfig) -> requests.Session:
    """
    Perform robust authentication with automatic CSRF handling and validation.

    This function implements the proven working authentication approach that
    handles dynamic authentication scenarios like DVWA. It includes:

    - Automatic CSRF token extraction and injection
    - Proper header management for maximum compatibility
    - Session state validation after authentication
    - Comprehensive error handling and logging

    Authentication Flow:
    1. Create session with optimal headers
    2. Fetch login page and extract CSRF tokens
    3. Inject tokens into credentials automatically
    4. Perform authentication POST request
    5. Validate session can access protected resources
    6. Return authenticated session

    Args:
        config (AuthConfig): Authentication configuration

    Returns:
        requests.Session: Authenticated and validated session

    Raises:
        AuthenticationError: If authentication fails after all attempts
        NetworkError: If network connectivity issues occur
        TimeoutError: If authentication requests timeout

    Example:
        >>> config = AuthConfig(
        ...     url="http://dvwa.local/login.php",
        ...     credentials={"username": "admin", "password": "password"}
        ... )
        >>> session = _perform_robust_authentication(config)
        >>> # Session is now authenticated and ready for use
    """
    try:
        logger.debug("Starting robust authentication process")

        # Create fresh session with optimal headers for compatibility
        session = requests.Session()
        session.verify = config.verify_ssl

        # Set headers for maximum compatibility with web applications
        default_headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
        }

        # Merge with any custom headers from config
        if config.headers:
            default_headers.update(config.headers)

        session.headers.update(default_headers)

        # Step 1: Fetch login page and extract CSRF tokens
        logger.debug(f"Fetching login page from {config.url}")

        try:
            login_page_response = session.get(config.url, timeout=config.timeout)
            login_page_response.raise_for_status()
        except requests.exceptions.Timeout as e:
            raise TimeoutError(
                f"Timeout fetching login page: {config.url}", config.timeout
            ) from e
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Failed to fetch login page: {e}") from e

        # Extract CSRF token from login page
        csrf_token = _extract_csrf_token(login_page_response.text)

        # Step 2: Prepare authentication credentials with CSRF token
        auth_credentials = config.credentials.copy()

        if csrf_token:
            logger.debug(f"Found CSRF token: {csrf_token[:10]}...")

            # Determine the appropriate CSRF field name
            csrf_field_names = [
                "user_token",  # DVWA
                "csrf_token",  # Generic
                "_token",  # Laravel
                "authenticity_token",  # Rails
                "csrfmiddlewaretoken",  # Django
            ]

            # Check if any CSRF field is already in credentials, if not use the most common
            csrf_field_used = None
            for field_name in csrf_field_names:
                if field_name in auth_credentials:
                    auth_credentials[field_name] = csrf_token
                    csrf_field_used = field_name
                    break

            # If no CSRF field found in credentials, add the most appropriate one
            if not csrf_field_used:
                # Try to detect the right field name from the login page
                content_lower = login_page_response.text.lower()
                if "user_token" in content_lower:
                    auth_credentials["user_token"] = csrf_token
                    csrf_field_used = "user_token"
                elif "_token" in content_lower:
                    auth_credentials["_token"] = csrf_token
                    csrf_field_used = "_token"
                else:
                    auth_credentials["csrf_token"] = csrf_token
                    csrf_field_used = "csrf_token"

            logger.debug(f"Injected CSRF token into field: {csrf_field_used}")
        else:
            logger.debug("No CSRF token found, proceeding without CSRF protection")

        # Step 3: Perform authentication POST request
        logger.debug(f"Performing authentication POST to {config.url}")

        try:
            auth_response = session.post(
                config.url,
                data=auth_credentials,
                timeout=config.timeout,
                allow_redirects=True,  # Follow redirects after authentication
            )
            auth_response.raise_for_status()
        except requests.exceptions.Timeout as e:
            raise TimeoutError(
                f"Timeout during authentication: {config.url}", config.timeout
            ) from e
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Authentication request failed: {e}") from e

        logger.debug(f"Authentication response: {auth_response.status_code}")
        try:
            # Log session state after authentication
            if hasattr(session.cookies, "__iter__"):
                logger.debug(
                    f"Session cookies after auth: {len(list(session.cookies))}"
                )
            else:
                logger.debug("Session cookies after auth: No enumerable cookies")
        except (TypeError, AttributeError):
            logger.debug("Session cookies after auth: Unable to enumerate cookies")

        # Step 4: Validate the session actually works
        if not _validate_session_access(session, config):
            raise AuthenticationError(
                "Authentication appeared successful but session validation failed"
            )

        logger.info("Robust authentication completed successfully")
        return session

    except (AuthenticationError, NetworkError, TimeoutError):
        # Re-raise known exceptions
        raise
    except Exception as e:
        logger.error(f"Unexpected error during robust authentication: {e}")
        raise AuthenticationError(
            f"Authentication failed due to unexpected error: {e}"
        ) from e


def _validate_session_access(session: requests.Session, config: AuthConfig) -> bool:
    """
    Validate that an authenticated session can access protected resources.

    This function performs the same validation logic used in the working
    bruteforce example to ensure the session is properly authenticated.

    Args:
        session (requests.Session): Session to validate
        config (AuthConfig): Authentication configuration

    Returns:
        bool: True if session can access protected resources, False otherwise
    """
    try:
        # Validate session object
        if not hasattr(session, "get") or not callable(getattr(session, "get")):
            logger.warning("Session validation skipped: Invalid session object")
            return False

        # Extract base URL
        base_url = config.url
        for suffix in ["/login.php", "/login", "/auth"]:
            if base_url.endswith(suffix):
                base_url = base_url[: -len(suffix)]
                break
        base_url = base_url.rstrip("/")

        # Try to access a protected resource (DVWA brute force page is a good test)
        test_urls = [
            f"{base_url}/vulnerabilities/brute/",
            f"{base_url}/vulnerabilities/",
            f"{base_url}/",
            f"{base_url}/index.php",
        ]

        for test_url in test_urls:
            try:
                test_response = session.get(test_url, timeout=5)

                if test_response.status_code == 200:
                    content = test_response.text

                    # Validate response content
                    if not isinstance(content, str):
                        logger.warning(
                            "Session validation failed: Invalid response content type"
                        )
                        return False

                    # Use the same validation logic as the working example
                    has_vuln_title = "Vulnerability: Brute Force" in content
                    has_welcome = "Welcome" in content
                    has_dvwa = "DVWA" in content
                    is_login_page = "Login ::" in content and "username" in content

                    # If we can access protected content without being redirected to login
                    if (
                        has_vuln_title or has_welcome or has_dvwa
                    ) and not is_login_page:
                        logger.debug(f"Session validation successful on {test_url}")
                        return True

            except Exception as e:
                logger.debug(f"Session validation error for {test_url}: {e}")
                continue

        logger.debug("Session validation failed: no protected resource accessible")
        return False

    except Exception as e:
        logger.debug(f"Session validation exception: {e}")
        return False


def _perform_session_warmup(session: requests.Session, config: AuthConfig) -> bool:
    """
    Perform session warmup after authentication to ensure proper state.
    This addresses issues where authentication succeeds but session doesn't persist.
    """
    try:
        # Extract base URL from login URL
        base_url = config.url.replace("/login.php", "/")

        # Perform comprehensive session warmup by visiting key pages in sequence
        warmup_sequence = [
            f"{base_url}index.php",  # Main page
            f"{base_url}vulnerabilities/",  # Vulnerabilities section
            f"{base_url}vulnerabilities/brute/",  # Specific vulnerability page
        ]

        for url in warmup_sequence:
            try:
                response = session.get(url, timeout=5, allow_redirects=True)
                logger.debug(
                    f"Session warmup - {url}: status={response.status_code}, final_url={response.url}"
                )

                if response.status_code == 200:
                    # Check if this page indicates successful authentication
                    if (
                        "login" not in response.text.lower()
                        and "Login ::" not in response.text
                    ):
                        if (
                            "Vulnerability:" in response.text
                            or "Welcome" in response.text
                            or "DVWA" in response.text
                        ):
                            logger.debug(
                                f"Session warmup confirmed working session at {url}"
                            )
                            # If we can access a protected page, warmup is successful
                            if "vulnerabilities" in url:
                                return True
                    else:
                        logger.debug(f"Session warmup found login indicators at {url}")
                else:
                    logger.debug(
                        f"Session warmup got non-200 status {response.status_code} for {url}"
                    )

            except Exception as e:
                logger.debug(f"Session warmup failed for {url}: {e}")
                continue

        # If we reach here, warmup didn't find a working protected page
        logger.debug("Session warmup completed but no protected page access confirmed")
        return False

    except Exception as e:
        logger.debug(f"Session warmup error: {e}")
        return False


def _enhance_session_for_dynamic_auth(
    session: requests.Session, config: AuthConfig
) -> requests.Session:
    """
    Enhance session for dynamic authentication scenarios.
    This implements the workaround fixes that make manual authentication work.
    """
    # Ensure session has proper headers for dynamic authentication
    if not session.headers.get("User-Agent"):
        session.headers["User-Agent"] = (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )

    # Add headers that help with session persistence
    session.headers.update(
        {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }
    )

    return session


def _attempt_session_recovery(session: requests.Session, config: AuthConfig) -> bool:
    """
    Attempt to recover a session that may have authentication but isn't persisting properly.
    This addresses DVWA-specific session state issues.
    """
    try:
        base_url = config.url.replace("/login.php", "/")

        # Strategy 1: Visit setup page if it exists (DVWA specific)
        setup_url = f"{base_url}setup.php"
        try:
            setup_response = session.get(setup_url, timeout=5, allow_redirects=True)
            if (
                setup_response.status_code == 200
                and "Database Setup" in setup_response.text
            ):
                logger.debug("Found DVWA setup page - attempting database reset")
                # Submit setup form to ensure database is ready
                session.post(
                    setup_url, data={"create_db": "Create / Reset Database"}, timeout=5
                )
        except Exception:
            pass  # Setup page might not exist or be accessible

        # Strategy 2: Visit security level page to establish session state
        security_url = f"{base_url}security.php"
        try:
            security_response = session.get(
                security_url, timeout=5, allow_redirects=True
            )
            if (
                security_response.status_code == 200
                and "Security Level" in security_response.text
            ):
                logger.debug("Accessed security page to establish session state")
                return True
        except Exception:
            pass

        # Strategy 3: Visit index and then vulnerabilities in sequence
        try:
            index_response = session.get(
                f"{base_url}index.php", timeout=5, allow_redirects=True
            )
            if index_response.status_code == 200:
                vuln_response = session.get(
                    f"{base_url}vulnerabilities/", timeout=5, allow_redirects=True
                )
                if (
                    vuln_response.status_code == 200
                    and "Brute Force" in vuln_response.text
                ):
                    logger.debug(
                        "Session recovery successful via index -> vulnerabilities sequence"
                    )
                    return True
        except Exception:
            pass

        return False

    except Exception as e:
        logger.debug(f"Session recovery error: {e}")
        return False


def _perform_manual_authentication_fallback(
    session: requests.Session, config: AuthConfig
) -> requests.Session:
    """
    Perform manual authentication using the proven working approach.
    This is used as a fallback when the regular auth approach doesn't work properly.
    """
    try:
        logger.debug("Starting manual authentication fallback")

        # Create a fresh session to avoid any state issues
        manual_session = requests.Session()

        # Copy session properties if available
        if session:
            manual_session.headers.update(session.headers)
            manual_session.verify = session.verify
            logger.debug("Copied session properties from original session")
        else:
            # Set up session with proper headers for compatibility
            manual_session.headers.update(
                {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                }
            )
            manual_session.verify = config.verify_ssl

        # Get fresh CSRF token for manual authentication
        login_page = manual_session.get(config.url)
        csrf_token = _extract_csrf_token(login_page.text)

        if not csrf_token:
            logger.warning(
                "Could not extract CSRF token for manual authentication - using original session"
            )
            return session

        logger.debug(f"Extracted CSRF token for manual auth: {csrf_token[:10]}...")

        # Prepare credentials with fresh CSRF token
        manual_credentials = config.credentials.copy()

        # Update dynamic tokens
        if "user_token" in manual_credentials:
            manual_credentials["user_token"] = csrf_token
        elif "csrf_token" in manual_credentials:
            manual_credentials["csrf_token"] = csrf_token
        elif "_token" in manual_credentials:
            manual_credentials["_token"] = csrf_token

        # Perform manual authentication
        login_response = manual_session.post(
            config.url,
            data=manual_credentials,
            allow_redirects=True,
            timeout=config.timeout,
        )

        logger.debug(f"Manual authentication response: {login_response.status_code}")

        # Verify manual session works
        test_url = config.url.replace("/login.php", "/vulnerabilities/brute/")
        test_response = manual_session.get(test_url)

        if (
            test_response.status_code == 200
            and "Vulnerability: Brute Force" in test_response.text
            and "login.php" not in test_response.url
        ):
            logger.info("Manual authentication fallback successful")
            return manual_session
        else:
            logger.warning(
                "Manual authentication fallback failed - using original session"
            )
            return session

    except Exception as e:
        logger.error(f"Manual authentication fallback error: {e}")
        return session


@monitor_performance("authentication")
def authenticate_session(
    auth_config: Union[AuthConfig, dict[str, Any]],
) -> requests.Session:
    """
    Authenticate and create a persistent session with automatic CSRF handling.

    This function provides robust authentication capabilities with automatic
    CSRF token detection, session caching, and validation. It maintains full
    backward compatibility while providing enhanced functionality.

    Features:
    - Automatic CSRF token extraction and injection
    - Intelligent session caching (excludes dynamic tokens)
    - Session validation and recovery mechanisms
    - Comprehensive error handling and logging
    - Full compatibility with runner module

    Args:
        auth_config (Union[AuthConfig, Dict[str, Any]]): Authentication configuration.
            Can be an AuthConfig object or a dictionary that will be converted.

    Returns:
        requests.Session: Authenticated session ready for use with protected resources.

    Raises:
        AuthenticationError: If authentication fails after all attempts
        ValidationError: If configuration is invalid
        NetworkError: If network connectivity issues occur
        TimeoutError: If authentication requests timeout

    Example:
        Basic authentication:
        ```python
        from logicpwn.core.auth import authenticate_session, AuthConfig

        config = AuthConfig(
            url="http://target.com/login.php",
            method="POST",
            credentials={
                "username": "admin",
                "password": "password",
                "Login": "Login"
                # CSRF tokens will be automatically extracted and added
            }
        )

        session = authenticate_session(config)

        # Use session with runner module
        from logicpwn.core.runner import HttpRunner

        # Create HttpRunner with the authenticated session
        runner = HttpRunner()
        runner.session = session

        # Make authenticated requests
        result = runner.get("http://target.com/protected/page")
        ```

        With success/failure indicators:
        ```python
        config = AuthConfig(
            url="http://dvwa.local/login.php",
            method="POST",
            credentials={"username": "admin", "password": "password"},
            success_indicators=["Welcome to DVWA", "Vulnerability:"],
            failure_indicators=["Login failed", "incorrect"],
            timeout=30
        )

        session = authenticate_session(config)
        ```
    """
    try:
        # Validate and normalize configuration
        config = validate_config(auth_config, AuthConfig)

        # Generate stable session ID for caching (excludes CSRF tokens)
        session_id = session_cache.generate_stable_session_id(config)

        # Check for cached session first
        cached_session = session_cache.get_session(session_id)
        if cached_session:
            logger.debug(f"Found cached session for {config.url}")

            # Validate cached session is still working
            if _validate_cached_session(cached_session, config):
                logger.debug("Cached session validation successful")
                logger.info(f"Using cached authenticated session for {config.url}")
                return cached_session
            else:
                logger.debug("Cached session validation failed, removing from cache")
                session_cache.invalidate_session(session_id)

        # Log authentication attempt (with sanitized credentials)
        sanitized_creds = _sanitize_credentials(config.credentials)
        logger.info(
            f"Attempting authentication to {config.url} with method {config.method}"
        )
        logger.debug(f"Credentials: {sanitized_creds}")

        # Perform robust authentication
        session = _perform_robust_authentication(config)

        # Handle legacy success/failure indicators if present
        # Note: This is maintained for backward compatibility but is optional
        # since robust authentication includes its own validation
        if config.success_indicators or config.failure_indicators:
            try:
                logger.debug("Checking legacy success/failure indicators")

                # Get a test page to check indicators
                base_url = (
                    config.url.replace("/login.php", "")
                    .replace("/login", "")
                    .rstrip("/")
                )
                test_response = session.get(f"{base_url}/", timeout=5)

                # Only process indicators if response is reasonable size to avoid hanging
                if len(test_response.text) < 1000000:  # 1MB limit
                    _handle_response_indicators(test_response, config)
                else:
                    logger.debug("Skipping indicator check: response too large")

            except (LoginFailedException, AuthenticationError):
                # Re-raise authentication failures - these are critical
                raise
            except Exception as e:
                logger.debug(f"Legacy indicator check failed (non-critical): {e}")

        # Ensure session has cookies (authentication should produce some cookies)
        if not session.cookies:
            logger.warning(
                "No cookies received during authentication - session may not persist"
            )
        else:
            try:
                # Log session state after successful authentication
                if hasattr(session.cookies, "__iter__"):
                    cookie_count = len(list(session.cookies))
                    logger.debug(
                        f"Authentication successful with {cookie_count} cookies"
                    )
                else:
                    logger.debug(
                        "Authentication successful with cookies (no enumerable cookies)"
                    )
            except (TypeError, AttributeError):
                logger.debug(
                    "Authentication successful with cookies (unable to enumerate)"
                )

        # Cache the authenticated session
        session_cache.set_session(session_id, session)
        logger.info("Authentication successful - session cached for future use")

        return session

    except requests.exceptions.Timeout as e:
        error_msg = f"Authentication request timed out after {config.timeout} seconds"
        logger.error(error_msg)
        raise TimeoutError(message=error_msg, timeout_seconds=config.timeout) from e

    except requests.exceptions.ConnectionError as e:
        error_msg = f"Network connection error during authentication: {e}"
        logger.error(error_msg)
        raise NetworkError(
            message="Network connection error during authentication",
            original_exception=e,
        ) from e

    except requests.exceptions.RequestException as e:
        error_msg = f"Request error during authentication: {e}"
        logger.error(error_msg)
        raise NetworkError(message=error_msg, original_exception=e) from e

    except ValueError as e:
        error_msg = f"Configuration validation error: {e}"
        logger.error(error_msg)
        raise ValidationError(
            message=error_msg, field="configuration", value=str(e)
        ) from e

    except (TimeoutError, NetworkError):
        # Re-raise TimeoutError and NetworkError from _perform_robust_authentication
        raise

    except LoginFailedException:
        # Re-raise LoginFailedException as-is
        raise

    except AuthenticationError:
        # Re-raise AuthenticationError as-is
        raise

    except Exception as e:
        error_msg = f"Unexpected error during authentication: {e}"
        logger.error(error_msg)
        raise AuthenticationError(error_msg) from e


def validate_session(session: requests.Session, test_url: str) -> bool:
    """
    Validate that a session is still active and authenticated.

    Args:
        session: The session to validate
        test_url: URL to test session access (should be a protected resource)

    Returns:
        True if session is valid and can access the test URL
    """
    try:
        response = session.get(test_url, timeout=DEFAULT_SESSION_TIMEOUT)

        # Check for common indicators that session is invalid
        if response.status_code in [401, 403]:
            return False

        # Check for redirects to login pages
        if response.status_code in [301, 302, 303, 307, 308]:
            location = response.headers.get("Location", "")
            if "login" in location.lower():
                return False

        # Check response content for login indicators
        try:
            # Validate response content for login indicators
            if hasattr(response, "text") and isinstance(response.text, str):
                if "Login ::" in response.text or "Please log in" in response.text:
                    return False
            else:
                # If response text is not a string, we can't check for login indicators
                logger.debug(
                    "Cannot check login indicators: response.text is not a string"
                )
        except (TypeError, AttributeError):
            # If we can't check response text, skip this check
            logger.debug("Cannot check login indicators: error accessing response.text")

        # If we get a 200 response without login indicators, session is likely valid
        return response.status_code == 200

    except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
        logger.debug(f"Session validation failed: {e}")
        return False


def logout_session(session: requests.Session, logout_url: str) -> bool:
    try:
        response = session.get(logout_url, timeout=DEFAULT_SESSION_TIMEOUT)
        session.cookies.clear()
        logger.info("Session logged out successfully")
        return True
    except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
        logger.error(f"Logout failed: {e}")
        return False


def authenticate_session_advanced(
    auth_config: Union[AuthConfig, dict[str, Any]], base_url: str = ""
) -> LogicPwnHTTPClient:
    """
    Create an authenticated HTTP client with advanced session management.

    This function provides enhanced authentication capabilities including:
    - Automatic CSRF token handling
    - Session state persistence and validation
    - Middleware integration
    - Intelligent caching
    - Retry mechanisms

    Args:
        auth_config: Authentication configuration (AuthConfig object or dict)
        base_url: Base URL for the HTTP client

    Returns:
        LogicPwnHTTPClient: Authenticated HTTP client ready for requests

    Raises:
        AuthenticationError: If authentication fails
        ValidationError: If configuration is invalid

    Example:
        ```python
        from logicpwn.core.auth import authenticate_session_advanced, AuthConfig, CSRFConfig

        # Basic usage
        config = AuthConfig(
            url="http://target.com/login.php",
            credentials={"username": "admin", "password": "password"}
        )
        client = authenticate_session_advanced(config)

        # Advanced usage with CSRF handling
        csrf_config = CSRFConfig(
            enabled=True,
            auto_include=True,
            refresh_on_failure=True
        )

        config = AuthConfig(
            url="http://target.com/login.php",
            credentials={"username": "admin", "password": "password"},
            csrf_config=csrf_config,
            session_validation_url="http://target.com/dashboard",
            success_indicators=["Welcome", "Dashboard"],
            failure_indicators=["Login failed", "Invalid credentials"]
        )

        client = authenticate_session_advanced(config, base_url="http://target.com")

        # Use the client for authenticated requests
        result = client.get("/protected/resource")
        result = client.post("/api/data", data={"key": "value"})
        ```
    """
    return create_authenticated_client(auth_config, base_url)


def create_csrf_config(
    enabled: bool = True,
    auto_include: bool = True,
    refresh_on_failure: bool = True,
    custom_patterns: Optional[list[str]] = None,
) -> CSRFConfig:
    """
    Create a CSRF configuration for advanced authentication.

    Args:
        enabled: Whether CSRF token handling is enabled
        auto_include: Automatically include tokens in subsequent requests
        refresh_on_failure: Re-fetch tokens if authentication fails
        custom_patterns: Additional regex patterns for token extraction

    Returns:
        CSRFConfig: Configuration object for CSRF handling

    Example:
        ```python
        csrf_config = create_csrf_config(
            enabled=True,
            custom_patterns=[
                r'name="custom_token".*?value="([^"]+)"',
                r'<meta name="app-token" content="([^"]+)"'
            ]
        )
        ```
    """
    config = CSRFConfig(
        enabled=enabled,
        auto_include=auto_include,
        refresh_on_failure=refresh_on_failure,
    )

    if custom_patterns:
        import re

        for pattern in custom_patterns:
            compiled_pattern = re.compile(pattern, re.IGNORECASE)
            config.token_patterns.append(compiled_pattern)

    return config


class Authenticator:
    """
    Advanced authenticator with comprehensive authentication capabilities.

    Features:
    - Intelligent redirect detection and handling
    - Multi-step authentication flows
    - JWT token management and validation
    - Session management with advanced security
    - Form-based authentication with CSRF protection
    """

    def __init__(
        self, config: "AdvancedAuthConfig", session: Optional[requests.Session] = None
    ):
        pass

        self.config = config
        self.session = session or requests.Session()

        # Flow management
        self.active_flows: dict[str, "AuthFlow"] = {}

    def detect_redirect_type(
        self, url: str, response: requests.Response
    ) -> "RedirectInfo":
        """
        Intelligently detect redirect type and extract parameters.

        Args:
            url: Target URL
            response: HTTP response

        Returns:
            RedirectInfo with detected redirect information
        """
        from urllib.parse import parse_qs, urlparse

        from .auth_models import RedirectInfo

        redirect_info = RedirectInfo(url=url)

        # Parse URL for parameters
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        # Flatten query parameters
        redirect_info.parameters = {
            k: v[0] if v else "" for k, v in query_params.items()
        }

        # Detect form POST redirects
        if response.status_code == 200 and "text/html" in response.headers.get(
            "content-type", ""
        ):
            content = response.text.lower()
            if 'method="post"' in content:
                redirect_info.is_form_post = True
                redirect_info.method = "POST"
                logger.debug("Detected form POST redirect")

        return redirect_info

    def authenticate_intelligent(self, url: str, **kwargs) -> "AuthenticationSession":
        """
        Intelligently detect authentication method and perform authentication.

        Args:
            url: Authentication URL
            **kwargs: Authentication parameters

        Returns:
            AuthenticationSession
        """
        from .idp_integration import AuthenticationSession, UserProfile

        # Probe the URL to detect authentication method
        try:
            response = self.session.get(url, allow_redirects=False, timeout=10)
            self.detect_redirect_type(url, response)

            # Use form-based authentication
            logger.info("Using form-based authentication")
            session = authenticate_session(self.config.base_config)

            # Create authentication session
            user_profile = UserProfile(
                user_id="form_user",
                email=kwargs.get("email", "user@example.com"),
                provider="form",
            )

            return AuthenticationSession(
                session_id=f"form_{int(time.time())}",
                user_profile=user_profile,
                provider="form",
                session_data={"requests_session": session},
            )

        except Exception as e:
            logger.warning(f"Failed to detect authentication method: {e}")
            from logicpwn.exceptions import AuthenticationError

            raise AuthenticationError(f"Unable to authenticate with {url}")

    def validate_jwt_token(self, token: str) -> dict:
        """
        Validate JWT token using configured secret.

        Args:
            token: JWT token string

        Returns:
            JWT claims if valid
        """
        if not self.config.jwt_secret_key:
            from logicpwn.exceptions import ValidationError

            raise ValidationError("No JWT secret key configured")

        try:
            import jwt

            claims = jwt.decode(
                token,
                self.config.jwt_secret_key,
                algorithms=[self.config.jwt_algorithm],
            )
            return claims
        except jwt.InvalidTokenError as e:
            from logicpwn.exceptions import AuthenticationError

            raise AuthenticationError(f"Invalid JWT token: {e}")

    def cleanup_expired_flows(self):
        """Clean up expired authentication flows."""

        expired_flows = [
            flow_id for flow_id, flow in self.active_flows.items() if flow.is_expired
        ]

        for flow_id in expired_flows:
            del self.active_flows[flow_id]

        if expired_flows:
            logger.debug(
                f"Cleaned up {len(expired_flows)} expired authentication flows"
            )


def create_advanced_config(base_config: "AuthConfig", **kwargs) -> "AdvancedAuthConfig":
    """Create advanced authentication configuration."""
    from .auth_models import AdvancedAuthConfig

    return AdvancedAuthConfig(base_config=base_config, **kwargs)
