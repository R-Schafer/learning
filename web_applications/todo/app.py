from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('todo.html', todos=[
        {"action": "feed dog", "done": True, "due": False},
        {"action": "eat breakfast", "done": False, "due": False},
        {"action": "eat lunch", "done": False, "due": True},
    ])