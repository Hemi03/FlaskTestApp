from json import loads

from ..conftests import test_client, init_database
from ...db_Model.models import Names


def testAllName(test_client, init_database):
    target = [["Test1", "Address1"], ["Test2", "Address2"]]
    response = test_client.get("/name")
    assert response.status_code == 200
    assert loads(response.json) == target


def testAllName_empty(test_client):
    response = test_client.get("/name")
    assert response.status_code == 200
    assert loads(response.json) == list()


def testGetName_Successfull(test_client, init_database):
    target = ["Test1", "Address1"]
    response = test_client.get("/name/Test1")
    assert response.status_code == 200
    assert loads(response.json) == target


def testGetName_NoNameGiven(test_client, init_database):
    response = test_client.get("/name/")
    assert response.status_code == 404


def testGetName_unknownName(test_client, init_database):
    response = test_client.get("/name/Test3")
    assert response.status_code == 404


def testPostName(test_client, init_database):
    target = ["Test3", "Address3"]
    response = test_client.post("/name/Test3", json={"Address": "Address3"})
    assert response.status_code == 200
    assert loads(response.json) == target
    assert Names.query.get("Test3").Address == "Address3"


def testPostName_noData(test_client, init_database):
    response = test_client.post("/name/Test3")
    assert response.status_code == 400


def testPostName_changeName(test_client, init_database):
    target = ["Test2", "Address3"]
    response = test_client.post("/name/Test2", json={"Address": "Address3"})
    assert response.status_code == 200
    assert loads(response.json) == target
    assert Names.query.get("Test2").Address == "Address3"


def testPostName_notDataForChange(test_client, init_database):
    response = test_client.post("/name/Test2")
    assert response.status_code == 400
