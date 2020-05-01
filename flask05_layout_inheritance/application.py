from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/seeMore")
def more():
    return render_template("seeMore.html")

