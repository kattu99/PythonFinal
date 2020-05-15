# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template('index.html')

#static route
@app.route("/books")
def books():
    return render_template('books.html')

#static route
@app.route("/classes")
def classes():
    return render_template('classes.html')

@app.route("/photo")
def photo():
    return render_template('Photo-Applying.jpg')

#start the server
if __name__ == "__main__":
    app.run()