from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture  # Arrange
def client():
    return TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá mundo!'}  # Assert


def test_hello_world_html(client):
    response = client.get('hello_html')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert (
        response.text
        == """
    <html>
        <head>
            <title> Olá mundo! </title>
        </head>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    """
    )


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }


def test_update_users(client):
    user_id = 1

    response = client.put(
        f'/users/{user_id}',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    response_error = client.put(
        '/users/0',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': user_id,
        'username': 'bob',
        'email': 'bob@example.com',
    }
    assert response_error.status_code == HTTPStatus.NOT_FOUND
    assert response_error.json() == {'detail': 'User not found'}


def test_delete_users(client):
    user_id = 1

    response = client.delete(f'/users/{user_id}')

    response_error = client.delete('/users/0')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}

    assert response_error.status_code == HTTPStatus.NOT_FOUND
    assert response_error.json() == {'detail': 'User not found'}
