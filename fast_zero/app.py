from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.routers import auth, todos, users
from fast_zero.schemas import Message

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/hello_html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hello_html():
    return """
    <html>
        <head>
            <title> Olá mundo! </title>
        </head>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    """
