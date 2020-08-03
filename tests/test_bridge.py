def test_404(client):
    root_response = client.get("/")
    assert root_response.status_code == 404
