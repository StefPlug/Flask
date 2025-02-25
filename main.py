from flask import Flask, url_for, request

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style2.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <center><h1>Анкета претендента</h1></center>
                            <center><p> на участие в миссии</p></center>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <p></p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <label for="education">Какое у Вас образование?</label>
                                    <p></p>
                                    <div class="form-group">
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    </select>
                                    <p></p>
                                    <label>Какие у Вас есть профессии?</label>
                                    <p></p>
                                    <div>
                                        <input type="checkbox" id="profession1" name="profession" value="Инженер-исследователь">
                                        <label for="profession1">Инженер-исследователь</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" id="profession2" name="profession" value="Инженер-строитель">
                                        <label for="profession2">Инженер-строитель</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" id="profession3" name="profession" value="Пилот">
                                        <label for="profession3">Пилот</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" id="profession4" name="profession" value="Метеоролог">
                                        <label for="profession4">Метеоролог</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" id="profession5" name="profession" value="Инженер по жизнеобеспечению">
                                        <label for="profession5">Инженер по жизнеобеспечению</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" id="profession6" name="profession" value="Инженер по радиационной защите">
                                        <label for="profession6">Инженер по радиационной защите</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" id="profession7" name="profession" value="Врач">
                                        <label for="profession7">Врач</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" id="profession8" name="profession" value="Экзобиолог">
                                        <label for="profession8">Экзобиолог</label>
                                    </div>
                                    
                                    <p></p>
                                    
                                    <label>Укажите пол:</label>
                                    <div>
                                        <input type="radio" id="male" name="gender" value="Мужской" required>
                                        <label for="male" class="warning">Мужской</label>
                                    </div>
                                    <div>
                                        <input type="radio" id="female" name="gender" value="Женский">
                                        <label for="female" class="warning">Женский</label>
                                    </div>
                                    
                                    <p></p>
                                    
                                    <div class="form-group">
                                        <label for="motivation">Почему Вы хотите принять участие в миссии?</label>
                                        <p></p>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    
                                    <p></p>
                                    
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <p></p>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <p></p>
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                        <p></p>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                        </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get('surname'))
        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('class'))
        print(request.form.get('profession'))
        print(request.form.get('gender'))
        print(request.form.get('file'))
        print(request.form.get('about'))
        print(request.form.get('accept'))
        return "Форма отправлена"
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
