from json import dumps

from flask_restful import Resource, reqparse

from ..db_Model import DB
from ..db_Model.models import Names


class Rest_AllNames(Resource):

    def get(self):
        names = Names.query.all()
        result = list()
        for i in names:
            result.append((i.Name, i.Address))
        return dumps(result)


class Rest_Name(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Address', type=str, required=True)

    def get(self, name: str):
        output = Names.query.get(name)
        if not output:
            return "Cant find Name", 404
        return dumps([output.Name, output.Address])

    def post(self, name: str):
        args = self.parser.parse_args()
        address = str(args['Address'])
        output = Names.query.get(name)
        if not output:
            output = Names.new_Names(name, address)
        else:
            if address == output.Address:
                return "cant change Address", 403
            output.Address = address
            output.commit()
        return output.toJson()

    def put(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def delete(self, name: str):
        target = Names.query.get(name)
        if not target:
            return "Cant find Name", 404
        target.delete()
