from flask import Flask, redirect, render_template, request

app = Flask(__name__)
DOG_NAMES = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "add_name" in request.form:
            dog_name = request.form['add_name']
            if dog_name.strip() != "":
                DOG_NAMES.append(dog_name)

        elif "delete_name" in request.form:
            dog_name = request.form['delete_name']
            DOG_NAMES.remove(dog_name)

    return render_template('index.html', dogs=DOG_NAMES)