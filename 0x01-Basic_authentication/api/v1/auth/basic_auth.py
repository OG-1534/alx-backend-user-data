#!/usr/bin/env python3
"""Module for API Basic authentication
"""

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
