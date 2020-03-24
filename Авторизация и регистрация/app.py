from flask import Flask
from flask import render_template
from flask import request, redirect
import sqlite3
import hashlib

# conn = sqlite3.connect("mydatabase.db")
# cursor = conn.cursor()
#
# cursor.execute("""CREATE TABLE user
#                  (id INTEGER AUTO_INCREMENT, login text, password text)
#               """)
# cursor.execute("""INSERT INTO user
#                   VALUES ('', 'admin', 'admin')"""
#                )
# conn.commit()
# conn.close()
#print(cursor.execute("""SELECT * FROM url""").fetchall())
#print(cursor.execute("""SELECT url FROM url WHERE short_url LIKE 'qwerty'""").fetchall()[0][0])
#conn.commit()

app = Flask(__name__)


# @app.route('/<string:short_url>', methods=['GET', 'POST'])
# def hello_world(short_url):
#     conn = sqlite3.connect("mydatabase.db")
#     cursor = conn.cursor()
#     redir = cursor.execute("""SELECT url FROM url WHERE short_url LIKE (?)""", (short_url,)).fetchall()[0][0]
#     return redirect(str(redir), code=302)

# @app.route('/', methods=['GET','POST'])
# def add():
#     conn = sqlite3.connect("mydatabase.db")
#     cursor = conn.cursor()
#     if request.method == 'GET':
#         return render_template('index.html')
#     if request.form['Добавить'] == 'Добавить':
#         url = request.form.get('url')
#         short_url = request.form.get('short_url')
#         cursor.execute("""INSERT INTO url (id,url,short_url) VALUES (?,?,?)""", ('',url,short_url))
#         conn.commit()
#         conn.close()
#         return ('Готово!')

@app.route('/', methods=['GET','POST'])
def add():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    if request.method == 'GET':
        return render_template('index.html')
    if request.form['Войти'] == 'Войти':
        login = str(request.form.get('login'))
        password = str(request.form.get('password'))
        if len(login) == 0 or len(password) == 0:
            return ('Поля не заполнены!')
        h = hashlib.md5(password.encode('utf-8'))
        hashPass = h.hexdigest()
        listuser = cursor.execute("""SELECT * FROM user""").fetchall()
        for x in listuser:
            if x[1] == login:
                if x[2] == hashPass:
                    return render_template('main.html')
                else:
                    return ('Ошибка! Пользователя не существует!')
            else:
                return ('Ошибка! Пользователя не существует!')




@app.route('/registration', methods=['GET','POST'])
def registration():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    if request.method == 'GET':
        return render_template('registration.html')
    if request.form['Добавить'] == 'Добавить':
        login = request.form.get('login')
        password = request.form.get('password')
        h = hashlib.md5(password.encode('utf-8'))
        hashPass = h.hexdigest()
        cursor.execute("""INSERT INTO user (id,login,password) VALUES (?,?,?)""", ('',login,hashPass))
        conn.commit()
        conn.close()
        return ('Готово!')


if __name__ == '__main__':
    app.run()