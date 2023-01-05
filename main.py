from flask import Flask, redirect, url_for, render_template, request
from get import find_data_by_query
app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("get_form"))


@app.get("/get_form")
def show_form():
    return render_template("show_form.html")


@app.post("/get_form")
def get_form():
    query = request.form['queryTemplate']

    return str(find_data_by_query(query)) + "<form action=\"/get_form\"><input type=\"submit\" value=\"Назад\" method=\"get\" /></form>"
