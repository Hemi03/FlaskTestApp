from unittest.mock import patch
from json import loads

from ...db_Model import DB
from ...db_Model.models import Names


@patch.object(DB.session, "add")
@patch.object(DB.session, "commit")
def testNewName(mock_commit, mock_add):
    test = Names.new_Names("Test", "Event")
    assert test.Name == "Test"
    assert test.Event == "Event"
    mock_add.assert_called_once_with(test)
    mock_commit.assert_called_once()


@patch.object(DB.session, "delete")
@patch.object(DB.session, "commit")
def testDeleteName(mock_commit, mock_delete):
    test = Names(Name="test", Event="event")
    test.delete()
    mock_delete.assert_called_once_with(test)
    mock_commit.assert_called_once()


def testToJson():
    target = {"Name": "test", "Event": "event"}
    name = Names(Name="test", Event="event")
    result = name.toJson()
    assert result == target
