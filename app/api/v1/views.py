"""Define API endpoints as routes"""

from flask_restful import Api, Resource

from . import v1_blueprint
from .resources import admin_endpoints, general_users_endpoints, store_attendant_endpoints

API = Api(v1_blueprint)

API.add_resource(admin_endpoints.ProductsManagement, '/products')
API.add_resource(general_users_endpoints.GeneralUsersActs, '/products')
API.add_resource(general_users_endpoints.SpecificProduct, '/products/<int:product_id>')
API.add_resource(store_attendant_endpoints.SaleRecords, '/saleorder')
API.add_resource(admin_endpoints.SaleAttendantsManagement, '/saleorder')