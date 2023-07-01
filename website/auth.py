from flask import Blueprint, render_template, request, flash, redirect, url_for
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

mydb = mysql.connector.connect(
    host = "107.20.93.40",
    user = "admin",
    password = "admin123",
    port = 3306,
    database = "pysite"
)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cursor = mydb.cursor()
        cursor.execute("SELECT password FROM users WHERE username = '%s'"%username)
        result = cursor.fetchall()
        pass_from_db = result
        cursor.execute("SELECT * FROM users WHERE username = '%s'"%username)
        user_exists = cursor.fetchall()
        print(pass_from_db)
        print(len(user_exists))
        if len(user_exists) != 0:
            pass_from_db = result[0]
            if check_password_hash(pass_from_db[0], password):
                flash('Logged in successfully!', category='success')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist.', category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM users WHERE username = '%s'"%username)
        db_result = cursor.fetchall()
        print(db_result)
        print(len(db_result))
        if len(db_result) != 0:
            flash('User already exists.', category='error')
        elif len(username) < 4:
            flash('Username must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 6:
            flash('Password must be greater than 5 characters', category='error')
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, generate_password_hash(password1, method='sha256')))
            mydb.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")