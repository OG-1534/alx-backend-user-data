#!/usr/bin/env python3
"""Module manages the API authentication
"""

from flask import request
from typing import List, TypeVar

class Auth:
    """Class that manages API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if endpoint requires authentication """
        return False

    def authorization_header(self, request=None) -> str:
        """ Retrieves authorization header from request """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current user from the request """
        return None

