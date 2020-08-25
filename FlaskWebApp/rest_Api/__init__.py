from flask_restful import Api

from .api_routes import Rest_AllNames, Rest_Name

API = Api()


def main():
    API.add_resource(Rest_Name, "/name/<string:name>")
    API.add_resource(Rest_AllNames, "/name")


if __name__ == "FlaskWebApp.rest_Api":
    main()
