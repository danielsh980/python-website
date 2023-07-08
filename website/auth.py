from flask import Blueprint, render_template, request, flash, redirect, url_for, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

mydb = mysql.connector.connect(
    host = "44.203.85.202",
    user = "admin",
    password = "admin123",
    port = 3306,
    database = "pysite"
)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        global sesh_user
        username = request.form.get('username')
        sesh_user = username
        password = request.form.get('password')

        cursor = mydb.cursor()
        cursor.execute("SELECT password FROM users WHERE username = '%s'"%username)
        result = cursor.fetchall()
        pass_from_db = result
        cursor.execute("SELECT * FROM users WHERE username = '%s'"%username)
        user_exists = cursor.fetchall()

        cursor.execute("SELECT * FROM users WHERE username = '%s'"%username)
        user = cursor.fetchone()

        print(len(user_exists))
        if len(user_exists) != 0:
            pass_from_db = result[0]
            if check_password_hash(pass_from_db[0], password):
                session['loggedin'] = True
                session['username'] = username
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist.', category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('auth.login'))

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

def getUsername():
    user = session['username']
    return user