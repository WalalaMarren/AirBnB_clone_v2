#!/usr/bin/python

from flask import Flask
app = Flask(__name__)
#A script that starts a flask application
#Your web application must be listening on 0.0.0.0, port 5000

@app.route('/')
def hbn():
    return “Hello HBNB!”

if __name__ == '__main__':
    app.run(debug=True)
