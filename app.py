from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)
app.secret_key = "your_secret_key"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/home-1")
def home_1():
    return render_template("home-1.html")


@app.route("/home-2")
def home_2():
    return render_template("home-2.html")


@app.route("/home-3")
def home_3():
    return render_template("home-3.html")


@app.route("/login")
def login():
    return render_template("login.html")



if __name__ == "__main__":
    app.run()
