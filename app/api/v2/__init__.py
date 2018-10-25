from flask import Blueprint


endpoint_v2_blueprint = Blueprint('endpoint_v2_blueprint', __name__)
auth_v2_blueprint = Blueprint('auth_v2_blueprint', __name__)



from . import views