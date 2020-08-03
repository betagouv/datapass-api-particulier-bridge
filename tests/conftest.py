import pytest
from bridge import create_app


@pytest.fixture
def client():
    app = create_app("bridge.config.TestingConfig")

    with app.test_client() as client:
        yield client
