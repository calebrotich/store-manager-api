"""
  Define API endpoints as routes
"""
from flask_restful import Api, Resource


# local imports
from . import v1_blueprint
from .resources import endpoints


API = Api(v1_blueprint)
API.add_resource(endpoints.add_product, '/')
