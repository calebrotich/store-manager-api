"""Define API endpoints as routes"""

from flask_restful import Api, Resource

from . import endpoint_v1_blueprint, auth_v1_blueprint
from .resources import admin_endpoints, general_users_endpoints, store_attendant_endpoints, auth

API = Api(endpoint_v1_blueprint)
AUTH_API = Api(auth_v1_blueprint)


API.add_resource(admin_endpoints.ProductsManagement, '/products')
API.add_resource(general_users_endpoints.AllProducts, '/products')
API.add_resource(general_users_endpoints.SpecificProduct, '/products/<int:product_id>')
API.add_resource(store_attendant_endpoints.SaleRecords, '/saleorder')
API.add_resource(admin_endpoints.SaleAttendantsManagement, '/saleorder')
API.add_resource(general_users_endpoints.SpecificSaleOrder, '/saleorder/<int:sale_order_id>')

AUTH_API.add_resource(auth.SignUp, '/signup')
AUTH_API.add_resource(auth.Login, '/login')