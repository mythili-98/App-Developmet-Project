from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

if __name__ == '__main__':
 app.run()
