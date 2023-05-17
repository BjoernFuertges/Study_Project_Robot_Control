
from flask import Flask, render_template, url_for

app = Flask("Robot Controls")

@app.route("/")
def index():
        return render_template('index.html')

@app.route("/controls")
def controls():
        return render_template('controls.html')


if __name__ == "__main__":
    app.run(debug=True)
