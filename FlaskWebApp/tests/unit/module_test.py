from ...db_Model.models import Names
from ..conftests import test_client, database


def testNewName(test_client, database):
    test = Names.new_Names("Test", "Address")
    assert test.Name == "Test"
    assert test.Address == "Address"
