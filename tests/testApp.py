import pytest

from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()    

def testApp(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200
    assert res.data == b"Hello MiniKube !"