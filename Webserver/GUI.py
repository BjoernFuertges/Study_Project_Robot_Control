
from flask import Flask, render_template, url_for
import requests

app = Flask("Robot Controls")

@app.route("/")
def index():
        return render_template('index.html')

@app.route("/controls")
def controls():
        return render_template('controls.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
        #Björn Funktionen
    return render_template('index.html', forward_message=forward_message);

@app.route("/backward/", methods=['POST'])
def move_backward():
    #Moving forward code
    backward_message = "Moving Back..."
    #Björn Funktionen
    return render_template('index.html', forward_message=backward_message);

@app.route("/leftturn/", methods=['POST'])
def turn_left():
    #Turn left code
    left_message = "Turning Left..."
        #Björn Funktionen

    return render_template('index.html', forward_message=left_message);

@app.route("/rightturn/", methods=['POST'])
def turn_right():
    #Moving forward code
    right_message = "Turning Right..."
        #Björn Funktionen

    return render_template('index.html', forward_message=right_message);


if __name__ == "__main__":
    app.run(debug=True)

