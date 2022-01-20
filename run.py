#! /usr/bin/env python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", data="data")

@app.route("/test")
def test():
    return render_template("test.html", data="data")

if __name__ == "__main__":
    app.run()