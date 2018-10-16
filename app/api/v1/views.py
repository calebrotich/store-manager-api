"""Define API endpoints as routes"""

from flask_restful import Api, Resource

from . import v1_blueprint
from .resources import admin_endpoints

API = Api(v1_blueprint)
API.add_resource(admin_endpoints.Product, '/products')