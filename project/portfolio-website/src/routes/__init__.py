from flask import Blueprint

routes = Blueprint('routes', __name__)

from . import portfolio_routes  # Assuming you will create a portfolio_routes.py for handling specific routes