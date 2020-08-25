from flask_restful import Api

from .api_routes import Rest_AllNames, Rest_Name

API = Api()
API.add_resource(Rest_Name, "/name/<string:name>")
API.add_resource(Rest_AllNames, "/name")
