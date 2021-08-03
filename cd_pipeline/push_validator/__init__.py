
from flask import Blueprint

validators = Blueprint('validator_blueprint', __name__)

from . import validator_views
