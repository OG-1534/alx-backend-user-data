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
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        path = path if path.endswith('/') else f"{path}/"

        for pattern in excluded_paths:
            if pattern.endswith('*'):
                if path.startswith(pattern[:-1]):
                    return False
            elif path == pattern or path == f"{pattern}/":
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves authorization header from request """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current user from the request """
        return None
