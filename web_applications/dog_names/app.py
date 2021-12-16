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

        elif "move_up" in request.form:
            dog_name = request.form['move_up']
            position = DOG_NAMES.index(dog_name)
            if position > 0:
                DOG_NAMES[position - 1], DOG_NAMES[position] = dog_name, DOG_NAMES[position - 1]

        elif "move_down" in request.form:
            dog_name = request.form['move_down']
            position = DOG_NAMES.index(dog_name)
            if position < len(DOG_NAMES) - 1:
                DOG_NAMES[position + 1], DOG_NAMES[position] = dog_name, DOG_NAMES[position + 1]

    return render_template('index.html', dogs=DOG_NAMES)