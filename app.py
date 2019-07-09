# Import files
from flask import Flask, request, render_template, flash, redirect, session, abort
from flaskext.mysql import MySQL
from flask import Markup
import os

# Creating instance of MySQL package
mysql = MySQL()
# Creating instance for flask
app = Flask(__name__)
app.secret_key = os.urandom(12)
# Mysql information
app.config['MYSQL_DATABASE_USER'] = 'phpmyadminuser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'demo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# Initiate app
mysql.init_app(app)

@app.route('/')
def my_form():
    if not session.get('logged_in'):
        return render_template('form_ex.html')
    else:
        #message = Markup('"Hello Boss!  <a href="/logout">Logout</a>"')
        #flash(message)
        return '<html><body>Hello Boss!  <a href="/logout">Logout</a></body></html>'

@app.route('/', methods = ['POST'])
def Authenticate():
    username = request.form['u']
    password = request.form['p']
    cursor = mysql.connect().cursor()
    stmt = "SELECT * from demo where username=%s and password=%s"
    data = (username,password)
    cursor.execute(stmt,data)
    data = cursor.fetchone()
    if data is None:
        flash("Username or password is wrong")
        return my_form()
    else:
        session['logged_in'] = True
        return my_form()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return my_form()

if __name__== "__main__":
    app.run()
