import functools
import config
from flask import Flask, session
from flask import redirect
from flask import request, make_response
from flask import render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from db import db
from app import app

'''
# 对app执行请求页面地址到函数的绑定
@app.route("/", methods=("GET", "POST"))
@app.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        # 客户端在login页面发起的POST请求
        username = request.form["username"]
        password = request.form["password"]
        ipaddr = request.form["ipaddr"]
        database = request.form["database"]

        db = db_login(username, password, ipaddr, database)

        if db is None:
            return render_template("login_fail.html")
        else:
            session['username'] = username
            session['password'] = password
            session['ipaddr'] = ipaddr
            session['database'] = database

            return redirect(url_for('table'))
    else:
        # 客户端GET 请求login页面时
        return render_template("login.html")


# 请求url为host/table的页面返回结果
@app.route("/table", methods=(["GET", "POST"]))
def table():
    # 出于简单考虑，每次请求都需要连接数据库，可以尝试使用其它context保存数据库连接
    if 'username' in session:
        db = db_login(session['username'], session['password'],
                      session['ipaddr'], session['database'])
    else:
        return redirect(url_for('login'))

    tabs = db_showtable(db)

    db_close(db)
    if request.method == "POST":
        if 'clear' in request.form:
            return render_template("table.html", rows='', dbname=session['database'])
        elif 'search' in request.form:
            return render_template("table.html", rows=tabs, dbname=session['database'])
        elif 'client_manage' in request.form:
            return redirect(url_for('client_manage'))
        elif 'account_manage' in request.form:
            return redirect(url_for('account_manage'))
        elif 'loan_manage' in request.form:
            return redirect(url_for('loan_manage'))
        elif 'business_count' in request.form:
            return redirect(url_for('business_count'))

    else:
        return render_template("table.html", rows=tabs, dbname=session['database'])


# client manage
@app.route("/client_manage", methods=(["GET", "POST"]))
def client_manage():
    if request.method == "POST":
        if 'go_back' in request.form:
            return redirect(url_for('table'))
    else:
        pass


# account manage
@app.route("/account_manage", methods=(["GET", "POST"]))
def account_manage():
    if request.method == "POST":
        if 'go_back' in request.form:
            return redirect(url_for('table'))
    else:
        pass
    # TODO: Add, Delete, Update, Check


# loan manage
@app.route("/loan_manage", methods=(["GET", "POST"]))
def loan_manage():
    if request.method == "POST":
        if 'go_back' in request.form:
            return redirect(url_for('table'))
    else:
        pass


# business_count
@app.route("/business_count", methods=(["GET", "POST"]))
def business_count():
    if request.method == "POST":
        if 'go_back' in request.form:
            return redirect(url_for('table'))
    else:
        pass


# 测试URL下返回html page
@app.route("/hello")
def hello():
    return "hello world!"
'''

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
