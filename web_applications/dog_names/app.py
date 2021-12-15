from flask import Flask, render_template, request

app = Flask(__name__)
DOG_NAMES = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        DOG_NAMES.append(request.form['dog_name'])

    return render_template('index.html', dogs=DOG_NAMES)