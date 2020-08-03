import pytest
from bridge import create_app


@pytest.fixture
def client():
    app = create_app("bridge.config.TestConfig")

    with app.test_client() as client:
        yield client
