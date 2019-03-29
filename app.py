import os
from flask import Flask, jsonify, render_template, request

__author__ = 'eps21'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
print(APP_ROOT)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        target = os.path.join(APP_ROOT, 'uploads/')
        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)

        for file in request.files.getlist("file"):
            print(file)
            filename = file.filename
            destination = "/".join([target, filename])
            print(destination)
            file.save(destination)

        msg = filename
        return render_template("briefer.html", msg = msg)


    elif request.method == 'GET':
        msg = 'file not uploaded'
        return render_template("briefer.html", msg = msg)


    # return render_template("complete.html")
    # return '''You have uploaded {}'''.format(filename)
    # return jsonify(filename = filename)
    #return render_template("briefer.html", msg=msg)

@app.route('/jinja_test')
@app.route('/jinja_test/<name>')
def jinja_test(name='Johnny'):
    if name == 'Johnny':
        name = 'jonnnny'
    elif name == 'Eric':
        name = 'eeerrrriic'
    return render_template('hello.html', name=name)

@app.route('/read_test')
def read_test():
    # directory of application uploads folder
    target = os.path.join(APP_ROOT, 'uploads/')
    text = open(target+'sample-paragraph.txt', 'r+') #wtf is r+ for?
    content = text.read()
    text.close()
    return render_template('readtest.html', text = content)


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


# example to upload files
@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'uploads/')
    print(target)


    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    msg = filename

    #return render_template("complete.html")
    #return '''You have uploaded {}'''.format(filename)
    # return jsonify(filename = filename)
    return render_template("briefer.html", msg = msg)


###################
# The other video #
###################

@app.route('/query_example')
def query_example():
    language = request.args.get('language')
    return '<h1>The language is: {}</h1>'.format(language)

@app.route('/form_example', methods=['POST', 'GET'])
def form_example():
    #basically like [HTTP post], if the method is post will return the post method here
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form['framework']
        return '<h1>The language is {}. The framework is {}</h1>'.format(language, framework)

    return '''<form method="POST">
    Language <input type="text" name="language">
    Framework <input type="text" name="framework">
    <input type="submit">
    </form>
    '''

# getting data from json
@app.route('/json_example', methods=['POST'])
def json_example():
    req_data = request.get_json()

    # handle a case where if a json value is empty
    language = None
    if 'language' in req_data:
        language = req_data['language']

    language = req_data['language']
    framework = req_data['framework']
    python_version = req_data['version_info']['python']
    form_example = req_data['examples'][0]
    boolean_test = req_data['boolean_test']

    return '''<h1>
    The language value is {}.
    The framework value is {}.
    The python version is {}.
    The example at 0 index is {}.
    The boolean value is {}.
    </h1>'''.format(language, framework, python_version, form_example, boolean_test)

# driver code
if __name__ == "__main__":
    app.run(port=4555, debug=True)