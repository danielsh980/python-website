from flask import Blueprint, render_template, request, flash, redirect, url_for, session
import mysql.connector
from website.auth import getUsername

actions = Blueprint('actions', __name__)

mydb = mysql.connector.connect(
    host = "54.172.195.249",
    user = "admin",
    password = "admin123",
    port = 3306,
    database = "pysite"
)

@actions.route('/store')
def store():
    return render_template("store.html")

@actions.route('/inventory', methods=['GET'])
def inventory():
    user = getUsername()
    cursor = mydb.cursor()
    cursor.execute("SELECT cola FROM users WHERE username = '%s'"%user)
    cola = ((cursor.fetchall())[0])[0]
    cursor.execute("SELECT water FROM users WHERE username = '%s'"%user)
    water = ((cursor.fetchall())[0])[0]
    cursor.execute("SELECT cola FROM users WHERE username = '%s'"%user)
    fanta = ((cursor.fetchall())[0])[0]

    total = (cola * 6) + (water * 2) + (fanta * 4)

    return render_template("inventory.html", cola=cola, water=water, fanta=fanta, total=total)

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
