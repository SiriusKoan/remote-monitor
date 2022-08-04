import pytest
from flask import url_for
from app import create_app


@pytest.fixture
def client():
    app = create_app("testing")
    client = app.test_client()
    app_context = app.app_context()
    app_context.push()
    yield client
    if app_context:
        app_context.pop()

def test_api_hosts(client):
    response = client.get(url_for("main.get_hosts_api"))
    assert response.status_code == 200


def test_api_func_results(client):
    response = client.get(
        url_for("main.get_results_api", host="test", func="test")
    )
    assert response.status_code == 200
