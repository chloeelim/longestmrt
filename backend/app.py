from flask import Flask, request, abort
from flask_cors import CORS

from graph import retrieve_longest_path, shortest_path

app = Flask(__name__)
CORS(app)

with open("../misc/data.csv") as f:
    data = [line.split(',') for line in f]
    codes = [i[0] for i in data]


def validate_stations(arg_start, arg_end):
    if not arg_start:
        return {"error": f"start is empty"}
    elif not arg_end:
        return {"error": f"end is empty"}

    start = [code for code in codes if arg_start.upper()
             in code.split()]
    end = [code for code in codes if arg_end.upper()
           in code.split()]
    if not start:
        return {"error": f"start {request.args['s']} is invalid"}
    if not end:
        return {"error": f"end {request.args['e']} is invalid"}
    start = start[0]
    end = end[0]
    return start, end


@app.route("/mrts")
def mrts():
    mrt = {}
    for codes, name, _, _ in data[1:]:
        for code in codes.split():
            mrt[code.lower()] = name
    return mrt


@app.route("/shortest")
def shortest():
    try:
        result = validate_stations(request.args["s"], request.args["e"])
        start, end = result
    except:
        return result, 400

    return {"path": shortest_path(start, end)}


@app.route("/longest")
def longest():
    try:
        result = validate_stations(request.args["s"], request.args["e"])
        start, end = result
    except:
        return result, 400

    return {"path": retrieve_longest_path(start, end)}
