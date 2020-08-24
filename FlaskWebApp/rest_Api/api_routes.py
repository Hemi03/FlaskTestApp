from flask_restful import Resource
from json import dumps

from ..db_Model import DB
from ..db_Model.models import Names

TEST_DATA = ["test1", "test2"]


class Rest_AllNames(Resource):

    def get(self):
        names = Names.query.all()
        result = list()
        for i in names:
            result.append((i.Name, i.Address))
        return dumps(result)


class Rest_Name(Resource):
    def post(self, name: str, address: str):
        Names.new_Names(name, address)
        return "success"

    def put(self, *args, **kwargs):
        self.post(*args, **kwargs)
