import pytest
import connexion
from dotenv import load_dotenv

# load dotenv
load_dotenv('.env')

# set up connexion
app = connexion.FlaskApp(__name__, specification_dir='../')
app.add_api('swagger.yml')


@pytest.fixture(scope='module')
def client():
    with app.app.test_client() as c:
        yield c


def test_get_comments(client):
    response = client.get('/api/comments')
    assert response.status_code == 200


def test_documentation_page(client):
    response = client.get('/api/ui')
    assert response.status_code == 200
