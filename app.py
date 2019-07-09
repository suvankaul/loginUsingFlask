# Import files
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

# Creating instance of MySQL package
mysql = MySQL()
# Creating instance for flask
app = Flask(__name__)
# Mysql information
app.config['MYSQL_DATABASE_USER'] = 'phpmyadminuser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'demo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# Initiate app
mysql.init_app(app)

@app.route('/')
def my_form():
    return render_template('form_ex.html')

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
        return "Username or password is wrong"
    else:
        return "Logged in Sucessfully"

if __name__== "__main__":
    app.run()
