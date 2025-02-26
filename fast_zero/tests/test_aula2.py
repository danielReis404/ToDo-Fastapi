from http import HTTPStatus

from fastapi.testclient import TestClient

from src.aula02 import app


def test_html_response():
    client = TestClient(app)

    response = client.get('/exercicio-html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text
