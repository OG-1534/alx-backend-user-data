#!/usr/bin/env python3
"""
Module for session authentication views
"""
from flask import jsonify, request, abort
from api.v1.auth.session_auth import SessionAuth
from api.v1.app import app_views


def logout_view():
    """ Handle DELETE /api/v1/auth_session/logout """
    auth = SessionAuth()
    if not auth.destroy_session(request):
        abort(404)

    return jsonify({})


# Register the logout view
app_views.add_url_rule('/auth_session/logout',
                       'logout_view',
                       logout_view, methods=['DELETE'])
