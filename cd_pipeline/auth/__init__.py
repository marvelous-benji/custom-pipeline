

from flask import Blueprint

server_auth = Blueprint('auth_blueprint', __name__)

from . import auth_view
