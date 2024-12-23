from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'cle',
            'email': 'cle@example.com',
            'password': 'secret',
        },
    )

    # assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'cle',
        'email': 'cle@example.com',
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
