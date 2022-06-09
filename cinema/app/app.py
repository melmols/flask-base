from flask import Flask, redirect, render_template, make_response, request
app = Flask(__name__)


@app.route("/")
def root():
    return render_template('/index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
