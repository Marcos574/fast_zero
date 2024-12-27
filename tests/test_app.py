from http import HTTPStatus


def test_read_root(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}


def test_hello_html(client):
    response = client.get('/hello_html')

    assert response.status_code == HTTPStatus.OK
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
