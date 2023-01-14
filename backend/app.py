from flask import Flask, request, abort
from flask_cors import CORS
from collections import deque
import json

from graph import longest_path

app = Flask(__name__)
CORS(app)

with open("../misc/data.csv") as f:
    data = [line.split(',') for line in f]
    codes = [i[0] for i in data]

with open("../misc/adj.json") as f:
    adj = json.load(f)


@app.route("/mrts")
def mrts():
    mrt = {}
    for codes, name, _, _ in data[1:]:
        for code in codes.split():
            mrt[code.lower()] = name
    return mrt

@app.route("/shortest")
def shortest():
    if "s" not in request.args or "e" not in request.args:
        abort(400)
    
    try:
        start = [code for code in codes if request.args['s'].upper() in code.split()]
        end = [code for code in codes if request.args['e'].upper() in code.split()]
        if not start:
            return {"error": f"start {request.args['s']} is invalid"}, 400
        if not end:
            return {"error": f"end {request.args['e']} is invalid"}, 400
        start = start[0]
        end = end[0]

    except:
        pass

    # bfs
    queue = deque()
    queue.append((start, None))
    parent = {}
    while queue:
        curr, par = queue.popleft()
        if curr in parent:
            continue
        else:
            parent[curr] = par
        
        if curr == end:
            break

        for edge in adj[curr]["edges"]:
            queue.append((edge, curr))
    res = []
    curr = end
    while curr:
        res.append(curr)
        curr = parent[curr]
    return { "path": res[::-1] }


@app.route("/longest")
def longest():
    if "s" not in request.args or "e" not in request.args:
        abort(400)
    try:
        start = [code for code in codes if request.args['s'].upper() in code.split()]
        end = [code for code in codes if request.args['e'].upper() in code.split()]
        if not start:
            return {"error": f"start {request.args['s']} is invalid"}, 400
        if not end:
            return {"error": f"end {request.args['e']} is invalid"}, 400
        start = start[0]
        end = end[0]
    except:
        abort(400)

    return { "path": longest_path(start, end) }
            
