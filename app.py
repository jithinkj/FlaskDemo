from flask import Flask, render_template, url_for  # import flask

app = Flask(__name__)  # create an app instance


@app.route("/hello")  # at the end point /
def hello():  # call method hello
    return "Hello World!"  # which returns "hello world"


@app.route("/jithin")  # at the end point /
def name():  # call method name
    return "Hello jithin!"  # which returns "hello world"

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)  # run the flask app
