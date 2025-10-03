"""
Generic JWT Authentication Backend for Label Studio

Authenticates users using JWT tokens from any external system.
Configurable via Django settings for maximum flexibility.
"""

import logging
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from jwt.exceptions import (
    InvalidTokenError,
    ExpiredSignatureError,
    InvalidSignatureError
)

logger = logging.getLogger(__name__)
User = get_user_model()


class JWTAuthenticationBackend(ModelBackend):
    """
    Generic JWT Authentication Backend for external SSO integration.

    Configuration (in Django settings.py):
        JWT_SSO_SECRET: JWT secret key for token verification (required)
        JWT_SSO_ALGORITHM: JWT algorithm (default: 'HS256')
        JWT_SSO_TOKEN_PARAM: URL parameter name for token (default: 'token')
        JWT_SSO_EMAIL_CLAIM: JWT claim containing user email (default: 'email')
        JWT_SSO_USERNAME_CLAIM: JWT claim containing username (optional, defaults to email)
        JWT_SSO_FIRST_NAME_CLAIM: JWT claim for first name (optional, default: 'first_name')
        JWT_SSO_LAST_NAME_CLAIM: JWT claim for last name (optional, default: 'last_name')
        JWT_SSO_AUTO_CREATE_USERS: Auto-create users if not found (default: False)

    Example configuration:
        JWT_SSO_SECRET = os.getenv('JWT_SSO_SECRET')
        JWT_SSO_ALGORITHM = 'HS256'
        JWT_SSO_TOKEN_PARAM = 'token'
        JWT_SSO_EMAIL_CLAIM = 'email'
        JWT_SSO_AUTO_CREATE_USERS = False
    """

    def authenticate(self, request, token=None, **kwargs):
        """
        Authenticate user using external JWT token.

        Args:
            request: HttpRequest object
            token: JWT token string from external system

        Returns:
            User object if authentication succeeds, None otherwise
        """
        # Extract token from URL parameter if not provided
        if not token and request:
            token_param = getattr(settings, 'JWT_SSO_TOKEN_PARAM', 'token')
            token = request.GET.get(token_param)

        if not token:
            logger.debug("No JWT token provided")
            return None

        # Get JWT configuration from settings
        jwt_secret = getattr(settings, 'JWT_SSO_SECRET', None)
        if not jwt_secret:
            logger.error("JWT_SSO_SECRET is not configured")
            return None

        jwt_algorithm = getattr(settings, 'JWT_SSO_ALGORITHM', 'HS256')
        email_claim = getattr(settings, 'JWT_SSO_EMAIL_CLAIM', 'email')
        username_claim = getattr(settings, 'JWT_SSO_USERNAME_CLAIM', None)
        first_name_claim = getattr(settings, 'JWT_SSO_FIRST_NAME_CLAIM', 'first_name')
        last_name_claim = getattr(settings, 'JWT_SSO_LAST_NAME_CLAIM', 'last_name')
        auto_create = getattr(settings, 'JWT_SSO_AUTO_CREATE_USERS', False)

        try:
            # Decode and verify JWT token
            payload = jwt.decode(
                token,
                jwt_secret,
                algorithms=[jwt_algorithm]
            )

            # Extract email from token
            email = payload.get(email_claim)
            if not email:
                logger.warning(f"JWT token does not contain '{email_claim}' claim")
                return None

            logger.info(f"JWT token verified for email: {email}")

            # Get username from token or use email
            username = payload.get(username_claim) if username_claim else email

            # Try to get existing user
            try:
                user = User.objects.get(email=email)
                logger.info(f"User found: {email}")

                # Update user info from JWT claims if available
                updated = False
                first_name = payload.get(first_name_claim, '')
                last_name = payload.get(last_name_claim, '')

                if first_name and user.first_name != first_name:
                    user.first_name = first_name
                    updated = True
                if last_name and user.last_name != last_name:
                    user.last_name = last_name
                    updated = True

                if updated:
                    user.save()
                    logger.info(f"Updated user info for: {email}")

                return user

            except User.DoesNotExist:
                if auto_create:
                    # Auto-create user
                    user = User.objects.create(
                        email=email,
                        username=username,
                        first_name=payload.get(first_name_claim, ''),
                        last_name=payload.get(last_name_claim, '')
                    )
                    logger.info(f"Auto-created user: {email}")
                    return user
                else:
                    logger.warning(f"User not found in Label Studio: {email}")
                    logger.info("Enable JWT_SSO_AUTO_CREATE_USERS or sync users manually")
                    return None

        except ExpiredSignatureError:
            logger.warning("JWT token has expired")
            return None
        except InvalidSignatureError:
            logger.error("JWT token signature verification failed")
            return None
        except InvalidTokenError as e:
            logger.error(f"Invalid JWT token: {str(e)}")
            return None
        except Exception as e:
            logger.exception(f"Unexpected error during JWT authentication: {str(e)}")
            return None

    def get_user(self, user_id):
        """
        Get user by ID (required by Django auth backend interface).
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


# Backward compatibility alias for Things-Factory
ThingsFactoryJWTBackend = JWTAuthenticationBackend
