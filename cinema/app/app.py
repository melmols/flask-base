from flask import Flask, redirect, render_template, make_response, request,  jsonify
import os

basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'static/flag.txt')

packets = []
with open(data_file, "r") as file:
    for line in file.readlines():
        packets.append(line.rstrip())

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('/index.html')
@app.route("/flag")
def flag():
    flag = "THM{P1Ng_0F_P1cTuR3H0Us3}"
    file_size = len(packets)
    if file_size > 550:
        return jsonify(flag)
    else:
        return render_template('/index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
