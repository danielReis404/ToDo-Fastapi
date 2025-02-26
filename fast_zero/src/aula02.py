from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/exercicio-html', response_class=HTMLResponse)
def aula02():
    return """<html>
      <head>
        <title>Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
