from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '''<p>Человечество вырастает из детства.</p>
<p>Человечеству мала одна планета.</p>
<p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
<p>И начнем с Марса!</p>
<p>Присоединяйся!</p>'''


@app.route('/image_mars')
def mars():
    return f'''<html>
    <head>
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='img/Mars.png')}">
        <p>Вот она какая, красная планета.</p>
    </body>
    </html>'''


@app.route('/promotion_image')
def prom_img():
    return f'''<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Колонизация</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" 
        rel="stylesheet" 
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" 
        crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='img/Mars.png')}">
        <div class="alert alert-secondary" role="alert">Человечество вырастает из детства.</div>
        <div class="alert alert-success" role="alert">Человечеству мала одна планета.</div>
        <div class="alert alert-secondary" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div>
        <div class="alert alert-warning" role="alert">И начнем с Марса!</div>
        <div class="alert alert-danger" role="alert">Присоединяйся!</div>
    </body>
    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
