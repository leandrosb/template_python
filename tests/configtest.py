from _pytest.python import Module
import pytest

from template import create_app

@pytest.fixture(scope='module')
def test_client():
    app = create_app('flask_test.cfg')
    with app.test_client() as testing_client:
        with app.app_context():
            yield test_client
