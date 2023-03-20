import random, string
from dbFunctions import *
from flask import make_response, jsonify
from datetime import datetime, timedelta

TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


def gen_code(length: int):
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


def datetime_to_string(dTime):
    dTime = dTime.strftime(TIMEFORMAT)
    return dTime


def time_plus_hours(dtime: datetime, h: int):
    newDtime = dtime + timedelta(hours=h)
    return newDtime


def user_session_validataion(userSessionID: str):
    try:
        userRow = get_row_from_table("userSessions", "userSessionID", userSessionID)
    except:
        print("[SERVER] - usersessionID not found in db")
        return False

    # check if sessionkey is expired
    currentTime = datetime.now()
    expiry = userRow[0][1]

    if expiry < currentTime:
        print("[SERVER] - Sessionkey expired!")
        return False

    return True


def lectureSesssion_validation(sessionID: str):

    try:
        userRow = get_row_from_table("lecturesessions", "sessionID", sessionID)
    except:
        print("[SERVER] - lectureSessionID not found in db")
        return False

    # check if sessionkey is expired
    currentTime = datetime.now()
    sessionStart = userRow[0][2]
    sessionEnd = userRow[0][3]

    if sessionStart > currentTime and sessionEnd < currentTime:
        print("[SERVER] - lectureSessionID expired!")
        return False

    return True
