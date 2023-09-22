#!/usr/bin/python
#Importing flask and starting up an application
from flask import Flask
app = Flask(__name__)
#A script that starts a flask application
#Your web application must be listening on 0.0.0.0, port 5000

@app.route('/')
def hbn():
    #function to return HBNB string
    return “Hello HBNB!”

if __name__ == '__main__':
    #enables debugging
    app.run(debug=True)
