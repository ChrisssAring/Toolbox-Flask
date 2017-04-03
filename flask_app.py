from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    name = (request.form['name'])
    age = request.form['age']
    favorite = (request.form['favorite'])
    if name and age and favorite:
        return render_template('user.html', user = name, age = age)
    else:
        return render_template('error.html')
