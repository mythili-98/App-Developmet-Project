from flask import Flask
from flask import render_template, request, redirect, url_for
from Forms import CreateUserForm

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/contact')
def contact():
    return render_template("contactUs.html")
@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/products')
def products():
    return render_template("products.html")
@app.route('/registration')
def registration():
    return render_template("registration.html")
@app.route('/search')
def search():
    return render_template("search.html")
@app.route('/brownmouse')
def brownmouse():
    return render_template("brownmouse.html")

if __name__ == '__main__':
 app.run()
