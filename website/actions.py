from flask import Blueprint, render_template, request, flash, redirect, url_for, session
import mysql.connector
from website.auth import getUsername

actions = Blueprint('actions', __name__)

mydb = mysql.connector.connect(
    host = "54.197.70.177",
    user = "admin",
    password = "admin123",
    port = 3306,
    database = "pysite"
)

@actions.route('/store')
def store():
    return render_template("store.html")

@actions.route('/cola', methods=['POST'])
def buyCola():
    user = getUsername()
    cursor = mydb.cursor()
    cursor.execute("SELECT cola FROM users WHERE username = '%s'"%user)
    quantity = ((cursor.fetchall())[0])[0] + 1
    cursor.execute("UPDATE users SET cola = %s WHERE username = %s", (quantity, user))
    mydb.commit()

    return render_template("store.html")

@actions.route('/water', methods=['POST'])
def buyWater():
    user = getUsername()
    cursor = mydb.cursor()
    cursor.execute("SELECT water FROM users WHERE username = '%s'"%user)
    quantity = ((cursor.fetchall())[0])[0] + 1
    cursor.execute("UPDATE users SET water = %s WHERE username = %s", (quantity, user))
    mydb.commit()

    return render_template("store.html")

@actions.route('/fanta', methods=['POST'])
def buyFanta():
    user = getUsername()
    cursor = mydb.cursor()
    cursor.execute("SELECT fanta FROM users WHERE username = '%s'"%user)
    quantity = ((cursor.fetchall())[0])[0] + 1
    cursor.execute("UPDATE users SET fanta = %s WHERE username = %s", (quantity, user))
    mydb.commit()

    return render_template("store.html")