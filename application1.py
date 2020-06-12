from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    headline = "Hellooooooo, world!"
    return render_template('ind.html', headline=headline)

@app.route("/bye")
def bye():
    headline = 'Goodbye!'
    return render_template('ind.html', headline=headline)
