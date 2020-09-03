from json import dumps

from flask_restful import Resource, reqparse
import logging

from ..db_Model import DB
from ..db_Model.models import Event


class Rest_AllEvent(Resource):
    def get(self):
        output = list()
        for i in Event.query.all():
            output.append(i.toJson())
        return output


class Rest_Event(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Theme', type=str, required=True)

    def get(self, event: str):
        output = Event.query.get(event)
        if not output:
            return "not event found", 404
        return output.toJson()

    def post(self, event: str):
        try:
            args = self.parser.parse_args()
        except ValueError as err:
            logging.exception(err)
            return "Broken Json Value", 400
        theme = str(args['Theme'])
        output = Event.query.get(event)
        if not output:
            output = Event.new_Event(event, theme)
        else:
            if theme == output.Theme:
                return "cant change Event", 403
            output.Theme = theme
            output.commit()
        return output.toJson()

    def put(self, *args, **kwargs):
        """redirect to post
        """
        return self.post(*args, **kwargs)

    def delete(self, event: str):
        target = Event.query.get(event)
        if not target:
            return False, 404
        target.delete()
        return True
