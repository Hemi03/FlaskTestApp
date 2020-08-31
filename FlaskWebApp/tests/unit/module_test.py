from unittest.mock import patch
from json import loads

from ...db_Model import DB
from ...db_Model.models import Names


@patch.object(DB.session, "add")
@patch.object(DB.session, "commit")
def testNewName(mock_commit, mock_add):
    test = Names.new_Names("Test", "Address")
    assert test.Name == "Test"
    assert test.Address == "Address"
    mock_add.assert_called_once_with(test)
    mock_commit.assert_called_once()


@patch.object(DB.session, "delete")
@patch.object(DB.session, "commit")
def testDeleteName(mock_commit, mock_delete):
    test = Names(Name="test", Address="address")
    test.delete()
    mock_delete.assert_called_once_with(test)
    mock_commit.assert_called_once()


def testToJson():
    target = ["test", "address"]
    name = Names(Name="test", Address="address")
    result = name.toJson()
    assert loads(result) == target
