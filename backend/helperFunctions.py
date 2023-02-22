import mysql.connector
import random, string


def dictionaryToTuple(dic):
    result = tuple(list(dic.values()))
    return result


def runDBQuery(query, val):
    with mysql.connector.connect(
        host="127.0.0.1", user="root", password="", database="sdgpTest"
    ) as myDB:
        myCursor = myDB.cursor()
        myCursor.execute(query, val)


def genCode():
    length = 5
    newCode = ""
    for i in range(length):
        newCode += random.choice(string.ascii_lowercase)
    return newCode


def extractRequiredData(receivedData, requiredData):
    outputData = {ed: receivedData[ed] for ed in requiredData}

    if len(outputData) != len(requiredData):
        raise Exception("Missing Values in POST")
    else:
        return outputData
