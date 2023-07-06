from flask import Blueprint, render_template, request, flash, redirect, url_for, session
import mysql.connector

actions = Blueprint('actions', __name__)

mydb = mysql.connector.connect(
    host = "3.84.251.250",
    user = "admin",
    password = "admin123",
    port = 3306,
    database = "pysite"
)

@actions.route('/store')
def store():
    return render_template("store.html")