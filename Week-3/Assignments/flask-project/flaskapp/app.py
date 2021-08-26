from flask import Flask, render_template, redirect, url_for, request, flash, make_response

from sum_n import sum_n_loop

# 主機、PORT 變數
DEBUG = True
PORT = 5000
HOST = 'localhost'

app = Flask(__name__)  # __name__ 代表目前執行的模組
app.secret_key = '601fa763dfeadd49fbd2556628170246'  # os.urandom(16).hex()


# Assignment 1
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', name='My Sever')


# Assignment 2
@app.route('/data', methods=['GET'])
def data():
    # 對使用者輸入的 number 取值
    number = request.args.get('number')
    if number:  # 如果存在
        try:  # 當可以轉成整數
            number = int(number)
            if number > 0:  # 比零大
                sum = sum_n_loop(number)  # 計算回傳
                return render_template(('data.html'), number=number, sum=sum)
            else:  # <= 0
                number = None
                flash("Wrong Parameter")
        except ValueError:  # 其他不能轉成整數的東西
            number = None
            flash("Wrong Parameter")
    else:  # number 不存在
        flash("Lack of Parameter")

    # 此時沒有 sum
    return render_template(('data.html'), number=number, sum=None)


# Assignment 3
@app.route('/sum', methods=('GET', 'POST'))
def sum_n():
    return render_template('sum.html')


# Assignment 4
# 有 view
@app.route('/myName', methods=['POST', 'GET'])
def my_name():
    # get cookie
    name = request.cookies.get('userID')
    # 如果可以拿到 cookie 就顯示
    if name:
        return '<h1>welcome ' + name + '</h1>'
    # 不能就顯示取值頁面
    else:
        return render_template('myName.html')


# 沒有 view 只供 set cookie
@app.route('/trackName', methods=['POST', 'GET'])
def track_name():
    # 如果從表單送出的 method 為 GET (會顯示在url上)
    if request.method == 'GET':
        # 從 name 取值(for GET)
        user = request.args.get('name')
        # 從 name 取值(for POST)
        # user = request.form['name']

        # 對重新導向的 myName.html 做回應
        resp = make_response(redirect(url_for('my_name')))
        # 回應為set cookie
        resp.set_cookie(key='userID', value=user)
        # 重新導向到 myName.html
        return resp


if __name__ == "__main__":  # 如果以主程式執行
    app.run(debug=DEBUG, host=HOST, port=PORT)  # 立即啟動伺服器
