from flask import Flask, redirect, render_template, make_response, request
from datetime import datetime

import uuid
import pickle
import base64

import sys

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('/index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=800)
