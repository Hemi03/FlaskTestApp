from flask_restful import Api

from .name_api import *
from .event_api import *

API = Api()


def main():
    """set up the API endpoints
    """
    API.add_resource(Rest_Name, "/name/<string:name>")
    API.add_resource(Rest_AllNames, "/name")
    API.add_resource(Rest_Event, "/event/<string:event>")
    API.add_resource(Rest_AllEvent, "/event")


if __name__ == "FlaskWebApp.rest_Api":
    main()
