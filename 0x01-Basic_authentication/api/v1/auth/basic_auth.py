#!/usr/bin/env python3
"""Module for API Basic authentication
"""

import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar, Tuple, Optional


class BasicAuth(Auth):
    """ BasicAuth class that inheriting from Auth. """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header.
        Returns None if the header is not valid.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        # Return the part after "Basic "
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string and returns its value as a UTF-8 string.
        Returns None if the input is invalid.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> Optional[Tuple[str, str]]:
        """
        Extracts user credentials from the Base64 decoded value.
        Returns a tuple (email, password).
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
            ) -> TypeVar('User'):
        """
        Retrieves the User instance based on email and password.
        """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None

        users = User.search({"email": user_email})
        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve the User instance for a request using Basic Authentication.
        """

        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None

        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_auth)
        if user_email is None or user_pwd is None:
            return None

        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
