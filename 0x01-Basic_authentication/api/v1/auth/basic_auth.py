#!/usr/bin/env python3
"""Module for API Basic authentication
"""

import base64
from typing import Tuple, Optional
from api.v1.auth.auth import Auth


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
