from json import loads

from ..conftests import test_client, init_database
from ...db_Model.models import Event


def testAllEvent(test_client, init_database):
    target = [{"Event": "Event1", "Theme": "Theme1"},
              {"Event": "Event2", "Theme": "Theme2"},
              {"Event": "Event3", "Theme": "Theme3"}]
    response = test_client.get("/event")
    assert response.status_code == 200
    assert response.json == target


def testAllEvent_empty(test_client):
    target = []
    response = test_client.get("/event")
    assert response.status_code == 200
    assert response.json == target


def testGetEvent(test_client, init_database):
    target = {"Event": "Event1", "Theme": "Theme1"}
    response = test_client.get("/event/Event1")
    assert response.status_code == 200
    assert response.json == target


def testGetEvent_unknown(test_client, init_database):
    response = test_client.get("/event/Event99")
    assert response.status_code == 404


def testGetEvent_noNameGiven(test_client, init_database):
    response = test_client.get("/event/")
    assert response.status_code == 404


def testPostEvent(test_client, init_database):
    target = {"Event": "Event4", "Theme": "Theme3"}
    response = test_client.post("/event/Event4", json={"Theme": "Theme3"})
    assert response.status_code == 200
    assert response.json == target
    assert Event.query.get("Event4").Theme == "Theme3"


def testPostEvent_change(test_client, init_database):
    target = {"Event": "Event1", "Theme": "Theme3"}
    response = test_client.post("/event/Event1", json={"Theme": "Theme3"})
    assert response.status_code == 200
    assert response.json == target
    assert Event.query.get("Event1").Theme == "Theme3"


def testPostEvent_noData(test_client, init_database):
    response = test_client.post("/event/Event4")
    assert response.status_code == 400


def testPostEvent_brokenJson(test_client, init_database):
    response = test_client.post("/event/Event4", json="{NONSENCE:")
    assert response.status_code == 400


def testPutEvent(test_client, init_database):
    target = {"Event": "Event4", "Theme": "Theme3"}
    response = test_client.post("/event/Event4", json={"Theme": "Theme3"})
    assert response.status_code == 200
    assert response.json == target
    assert Event.query.get("Event4").Theme == "Theme3"


def testDeleteEvent(test_client, init_database):
    response = test_client.delete("/event/Event3")
    assert response.status_code == 200
    assert response.json == True
    assert Event.query.get("Event3") == None


def testDeleteEvent_tryUsedEvent(test_client, init_database):
    response = test_client.delete("/event/Event2")
    assert response.status_code == 400
    assert response.json == False


def testDeleteEvent_unknownEvent(test_client, init_database):
    response = test_client.delete("/event/Event99")
    assert response.status_code == 404
    assert response.json == False


def testDeleteEvent_noEvent(test_client, init_database):
    response = test_client.delete("/event/")
    assert response.status_code == 404
