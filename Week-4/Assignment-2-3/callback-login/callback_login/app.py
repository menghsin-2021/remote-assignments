from flask import Flask, render_template, request, flash, make_response, redirect, url_for
import models
import config

# sever var
DEBUG = config.DEBUG
PORT = config.PORT
HOST = config.HOST
SECRET_KEY = config.SECRET_KEY

# db var
DBHOST = config.DBHOST
DBUSER = config.DBUSER
DBPASSWORD = config.DBPASSWORD
DBNAME = config.DBNAME
TABLES = config.TABLES
TBNAME = config.TBNAME

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', name='My Sever')


@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')  # form name='email'
    pwd = request.form.get('pwd')
    con_pwd = request.form.get('con-pwd')
    # 搜尋是否有相同的email
    sql = "SELECT `id` FROM `user` WHERE `email`= %s"
    connect_db = models.connect_db(DBHOST, DBUSER, DBPASSWORD, db_name='assignment')
    cursor = connect_db.cursor()
    cursor.execute(sql, (email,))
    result = cursor.fetchone()
    if email and pwd and not result and pwd == con_pwd:
        sql = "INSERT INTO `user` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, (email, pwd))
        connect_db.commit()
        connect_db.close()
        flash('signup success')
    else:
        connect_db.close()
        flash('email is exist or confirmation password error')
    return render_template('index.html')

@app.route('/signin', methods=['POST'])
def signin():
    email = request.form.get('email')
    pwd = request.form.get('pwd')
    # 搜尋是否有註冊帳號且輸入正確密碼
    sql = "SELECT `email`, `password` FROM `user` WHERE `email`= %s"
    connect_db = models.connect_db(DBHOST, DBUSER, DBPASSWORD, db_name='assignment')
    cursor = connect_db.cursor()
    cursor.execute(sql, (email,))
    result = cursor.fetchone()
    connect_db.close()
    if result:
        if email == result[0] and pwd == result[1]:
            resp = make_response(redirect(url_for('welcome')))
            # 回應為set cookie
            resp.set_cookie(key='user', value=email.split('@')[0])
            # 重新導向到 welcome.html
            return resp
    flash('wrong password or email is not exist')
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    # get cookie
    name = request.cookies.get('user')
    # 如果可以拿到 cookie 就顯示
    if name:
        return '<h1>welcome ' + name + '</h1>'
    # 不能就回首頁
    else:
        return render_template('index.html')



if __name__ == "__main__":  # 如果以主程式執行
    # db initialize
    connect_db = models.connect_db(DBHOST, DBUSER, DBPASSWORD)  # mysql 連線
    cursor = connect_db.cursor()  # 建立鼠標
    cursor = models.create_db(cursor, DBNAME=DBNAME)  # 建立新資料庫(資料庫存在就不建)
    models.create_tb(cursor, TABLES=TABLES, TBNAME=TBNAME)  # 建立 table (table存在就不建)
    connect_db.close()  # 關閉資料庫連線
    # run sever
    app.run(debug=DEBUG, host=HOST, port=PORT)