

from flask import Blueprint

push_event = Blueprint('push_blueprint', __name__)

from . import push_view
