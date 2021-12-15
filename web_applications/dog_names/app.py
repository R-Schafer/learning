from flask import Flask, render_template, request

app = Flask(__name__)
DOG_NAMES = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        dog_name = request.form['dog_name']
        if dog_name.strip() != "":
            DOG_NAMES.append(dog_name)

    return render_template('index.html', dogs=DOG_NAMES)