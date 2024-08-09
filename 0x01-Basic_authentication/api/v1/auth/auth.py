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

        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Ensure path ends with a slash
        if path[-1] != '/':
            path += '/'

        # Ensure path is in excluded_paths
        if path in excluded_paths:
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
