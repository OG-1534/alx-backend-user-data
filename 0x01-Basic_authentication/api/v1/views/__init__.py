from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from api.v1.views import index
from api.v1.views import users

__all__ = ['app_views']
