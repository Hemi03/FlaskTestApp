import pytest

from .. import create_app
from ..config import TestingConfig
from ..db_Model import DB
from ..db_Model.models import Names


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app(TestingConfig)
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture
def init_database():
    # Insert user data
    name1 = Names.new_Names("Test1", "Address1")
    name2 = Names.new_Names("Test2", "Address2")

    yield DB  # this is where the testing happens!

    DB.drop_all()
    DB.create_all()


@pytest.fixture
def database():
    DB.create_all()
    yield DB
    DB.drop_all()
