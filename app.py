import os
from flask import Flask, jsonify, render_template, request

__author__ = 'eps21'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("briefer.html")


@app.route('/add_numbers')
def add_numbers():
    #0 is default value in case it fails to get 'a' or 'b'
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result = a + b)

@app.route('/analyze_text_area')
def analyze():
    textvar = request.args.get('text', 0, type=str)
    append = 'lalala'
    return jsonify(textresult = textvar + append)


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")

if __name__ == "__main__":
    app.run(port=4555, debug=True)