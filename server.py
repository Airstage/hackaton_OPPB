from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def index():
    if request.method == 'GET':
        log, pas = request.args['login'], request.args['password']
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        query = f'''SELECT * FROM users WHERE login = "{log}" AND password = "{pas}"'''
        data = cur.execute(query).fetchall()
        if data:
            print(data)
            return {'answer': 'Вошли успешно.'}
        else:
            print('Нет такого пользователя.')
            return {'answer': 'Ошибка. Неверный логин/пароль.'}


app.run()