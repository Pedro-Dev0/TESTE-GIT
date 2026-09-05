import pytest
from src import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "SECRET_KEY":"test",
            "SQLALCHEMY_DATABASE_URI":"sqlite://",
            "JWT_SECRET_KEY":"test",
        }
    )
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()