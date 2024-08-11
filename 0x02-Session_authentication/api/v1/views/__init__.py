#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import create_session_view
from models.user import User

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


# Register the new route
app_views.add_url_rule('/auth_session/login',
                       'create_session_view',
                       create_session_view, methods=['POST'])

# Load user data
User.load_from_file()
