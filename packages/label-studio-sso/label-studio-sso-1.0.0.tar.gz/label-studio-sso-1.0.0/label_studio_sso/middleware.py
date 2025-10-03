"""
Generic JWT Auto-Login Middleware

Automatically logs in users when they access Label Studio with a valid JWT token.
"""

import logging
from django.contrib.auth import login
from django.conf import settings
from .backends import JWTAuthenticationBackend

logger = logging.getLogger(__name__)


class JWTAutoLoginMiddleware:
    """
    Middleware to automatically log in users via JWT token.

    When a request contains a valid JWT token in the URL parameter,
    this middleware authenticates the user and establishes a session.

    Configuration (in Django settings.py):
        JWT_SSO_TOKEN_PARAM: URL parameter name for token (default: 'token')
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.backend = JWTAuthenticationBackend()

    def __call__(self, request):
        # Skip if user is already authenticated
        if request.user.is_authenticated:
            logger.debug(f"User already authenticated: {request.user.email}")
            return self.get_response(request)

        # Check for JWT token in URL parameters
        token_param = getattr(settings, 'JWT_SSO_TOKEN_PARAM', 'token')
        token = request.GET.get(token_param)

        if not token:
            # No token, proceed normally
            return self.get_response(request)

        logger.info("JWT token detected in URL, attempting auto-login")

        # Attempt to authenticate with JWT token
        user = self.backend.authenticate(request, token=token)

        if user:
            # Log in the user
            login(
                request,
                user,
                backend='label_studio_sso.backends.JWTAuthenticationBackend'
            )
            logger.info(f"User auto-logged in: {user.email}")
        else:
            logger.warning("JWT token authentication failed")

        # Continue processing the request
        response = self.get_response(request)
        return response


# Backward compatibility alias for Things-Factory
ThingsFactoryAutoLoginMiddleware = JWTAutoLoginMiddleware
