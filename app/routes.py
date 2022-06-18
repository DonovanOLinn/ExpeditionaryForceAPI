from app import app
from flask import render_template




@app.route('/')
def home():
    greeting='hello, Foxes!'
    print(greeting)

    return render_template('index.html')
