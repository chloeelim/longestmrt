from flask import Flask

app = Flask(__name__)

with open("../misc/data.csv") as f:
    data = [line.split(',') for line in f]


@app.route("/mrts")
def mrts():
    mrt = {}
    for codes, name, _, _ in data[1:]:
        for code in codes.split():
            mrt[code.lower()] = name
    return mrt


app.run(debug=True)
