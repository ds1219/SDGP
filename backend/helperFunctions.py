import random, string
from dbFunctions import *
from flask import make_response, jsonify


def gen_code():
    length = 5
    newCode = ""
    for i in range(length):
        newCode += random.choice(string.ascii_lowercase)
    return newCode


def extract_required_data(receivedData, requiredData):
    outputData = {ed: receivedData[ed] for ed in requiredData}

    if len(outputData) != len(requiredData):
        raise Exception("Missing Values in POST")
    else:
        return outputData


def server_response(
    status: int,
    json: dict = {},
):
    if json != {}:
        json = jsonify(json)
        response = make_response(json)
    else:
        response = make_response()

    response.status_code = status

    return response
