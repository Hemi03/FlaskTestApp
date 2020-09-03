from json import loads

from ..conftests import test_client, init_database
from ...db_Model.models import Names


def testAllName(test_client, init_database):
    target = [{"Name": "Test1", "Event": "Event1"},
              {"Name": "Test2", "Event": "Event2"}]
    response = test_client.get("/name")
    assert response.status_code == 200
    assert response.json == target


def testAllName_empty(test_client):
    response = test_client.get("/name")
    assert response.status_code == 200
    assert response.json == list()


def testGetName(test_client, init_database):
    target = {"Name": "Test1", "Event": "Event1"}
    response = test_client.get("/name/Test1")
    assert response.status_code == 200
    assert response.json == target


def testGetName_NoNameGiven(test_client, init_database):
    response = test_client.get("/name/")
    assert response.status_code == 404


def testGetName_unknownName(test_client, init_database):
    response = test_client.get("/name/Test3")
    assert response.status_code == 404


def testPostName(test_client, init_database):
    target = {"Name": "Test3", "Event": "Event3"}
    response = test_client.post("/name/Test3", json={"Event": "Event3"})
    assert response.status_code == 200
    assert response.json == target
    assert Names.query.get("Test3").Event == "Event3"


def testPostName_noData(test_client, init_database):
    response = test_client.post("/name/Test3")
    assert response.status_code == 400


def testPostName_changeName(test_client, init_database):
    target = {"Name": "Test2", "Event": "Event3"}
    response = test_client.post("/name/Test2", json={"Event": "Event3"})
    assert response.status_code == 200
    assert response.json == target
    assert Names.query.get("Test2").Event == "Event3"


def testPostName_notDataForChange(test_client, init_database):
    response = test_client.post("/name/Test2")
    assert response.status_code == 400


def testPostName_brokenJson(test_client, init_database):
    response = test_client.post("/name/Test3", json="{NONSENSE")
    assert response.status_code == 400


def testPutName(test_client, init_database):
    target = {"Name": "Test3", "Event": "Event3"}
    response = test_client.put("/name/Test3", json={"Event": "Event3"})
    assert response.status_code == 200
    assert response.json == target
    assert Names.query.get("Test3").Event == "Event3"


def testDeleteName(test_client, init_database):
    response = test_client.delete("/name/Test1")
    assert response.status_code == 200
    assert response.json == True
    assert Names.query.get("Test1") == None


def testDeleteName_unknownName(test_client, init_database):
    response = test_client.delete("/name/Test3")
    assert response.status_code == 404
    assert response.json == False


def testDeleteName_noName(test_client, init_database):
    response = test_client.delete("/name/")
    assert response.status_code == 404
    assert response.json == False
