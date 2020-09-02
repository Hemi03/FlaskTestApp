from json import dumps

from flask_restful import Resource, reqparse
import logging

from ..db_Model import DB
from ..db_Model.models import Names


class Rest_AllNames(Resource):
    """The Api Object for /name
    """

    def get(self):
        """return a List of all Names

        Returns:
            list: a List of Names z.B. [{"Name": name, "Address": address}]
        """
        names = Names.query.all()
        result = list()
        for i in names:
            result.append(i.toJson())
        return result


class Rest_Name(Resource):
    """The Api for /name/[name]
    """
    parser = reqparse.RequestParser()
    parser.add_argument('Address', type=str, required=True)

    def get(self, name: str):
        """return data for the given Name as Json

        Args:
            name (str): the Name to query

        Returns:
            dict: the Name as Json or Error
        """
        output = Names.query.get(name)
        if not output:
            return "Cant find Name", 404
        return output.toJson()

    def post(self, name: str):
        """create a new Name Database Entry or try to change an existing one

        Args:
            name (str): the Name to crate or change

        Returns:
            dict: return created/changed Name as Json or Error
        """
        try:
            args = self.parser.parse_args()
        except ValueError as err:
            logging.exception(err)
            return "Broken Json Value", 400
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
        """redirect to post
        """
        return self.post(*args, **kwargs)

    def delete(self, name: str):
        """try to Delete the given Name

        Args:
            name (str): Name to delete

        Returns:
            bool: true for success or false for fail
        """
        target = Names.query.get(name)
        if not target:
            return False, 404
        target.delete()
        return True
