#!/usr/bin/env python3
"""
Module for session authentication views
"""
from base64 import b64decode
import uuid
from typing import Optional, TypeVar
from flask import jsonify, request, make_response
from api.v1.auth.auth import Auth
from models.user import User
from api.v1.auth.session_auth import SessionAuth


class SessionAuth(Auth):
    """
    Session authentication class that inherits from Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Method creates a session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> Optional[User]:
        """Returns the User instance based on a cookie value"""
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

    def create_session_view():
    """ Handle POST /api/v1/auth_session/login """
    email = request.form.get('email')
    password = request.form.get('password')

    # To validate email
    if not email:
        return jsonify({"error": "email missing"}), 400

    # To validate password
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Retrieve User instance based on email
    user = User.search(email=email)
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    # Validate password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create Session ID
    auth = SessionAuth()
    session_id = auth.create_session(user.id)

    # Create response
    response = make_response(user.to_json())
    cookie_name = request.environ.get('SESSION_NAME', '_my_session_id')
    response.set_cookie(cookie_name, session_id)

    return response
