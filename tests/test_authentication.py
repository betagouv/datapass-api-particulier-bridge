def test_404(client):
    root_response = client.get("/")
    assert root_response.status_code == 404


def test_subscribe_route_authentication_failure(client):
    subscribe_request = client.post("/applications/subscribe")
    assert subscribe_request.status_code == 401


def test_invalid_api_key(client):
    subscribe_request = client.post(
        "/applications/subscribe", headers={"X-Gravitee-API-Key": "lol"}
    )
    assert subscribe_request.status_code == 403


def test_valid_api_key(client):
    subscribe_request = client.post(
        "/applications/subscribe", headers={"X-Gravitee-API-Key": "test_api_key"}
    )
    assert subscribe_request.status_code == 200
