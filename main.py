from flask import Flask, make_response, jsonify
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def getTime():
    temp = round(random.uniform(20.01, 24.99), 2)
    temp = str(temp)
    resp = make_response(
        jsonify(
            {
                "author": "ODIK Y N",
                "title": "Learn IoT",
                "description": "Free 3 month only, just testing api from pythonanywhere using flask",
                "webapi": "nugroho.pythonanywhere.com",
                "temperature": "{}".format(temp),
                "satuan": "C",
            }
        ),
        200,
    )

    return resp, {"Access-Control-Allow-Origin": "*"}


@app.route("/api/<s>", methods=["POST"])
def getApi(s):
    return {"message": "Successfully!", "temperature": str(s)}
