import json
from datetime import datetime

import pytest
from dotenv import load_dotenv

from app import create_app, db
from app.models import Comment
from config import TestingConfig

# load dotenv
load_dotenv(".env")


@pytest.fixture(scope="module")
def application():
    app = create_app(TestingConfig)

    with app.app.app_context():
        yield app.app


@pytest.fixture(scope="module")
def database(application):

    # Insert comment data
    comment1 = Comment(
        sku="1",
        text="i like it",
        owner="john",
        timestamp=datetime(2017, 3, 3, 0, 0, 0),
        tone="positive",
    )
    comment2 = Comment(
        sku="2",
        text="i hate it",
        owner="doe",
        timestamp=datetime(2018, 4, 4, 0, 0, 0),
        tone="negative",
    )

    db.session.add(comment1)
    db.session.add(comment2)

    # Commit the changes for the comments
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope="module")
def client(application):
    with application.test_client() as c:
        yield c


def test_get_comments(database, client):
    response = client.get("/api/comments")
    assert response.status_code == 200
    assert "i like it" in str(response.data)


def test_documentation_page(database, client):
    response = client.get("/api/ui", follow_redirects=True)
    assert response.status_code == 200


def test_comments_in_database(database):
    comments = Comment.query.all()
    assert len(comments) == 2


def test_add_new_comment(database, client):
    response = client.post(
        "/api/comments", data=dict(sku="3", text="not very good", owner="person")
    )

    data = json.loads(response.data)

    assert response.status_code == 201
    assert data["id"] == "3"
    assert Comment.query.count() == 3
