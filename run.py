import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/careers')
def careers():
    return render_template("careers.html")

<<<<<<< HEAD
@app.route('/base')
def base():
    return render_template("base.html")

=======
>>>>>>> 3b243634b1179f15bd8c99196c42925a5b2a4e18
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)