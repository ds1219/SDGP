from dbFunctions import *
from helperFunctions import gen_code
from time import sleep
from questionGenerator import generate

jobs = []


def run_ml(text):
    print(text)
    sleep(2)
    return ("Q", "A", "WA")


def check_for_jobs():
    sql = "SELECT sessionID, questionSource FROM lectureSessions WHERE sessionID NOT IN (SELECT sessionID FROM questions);"
    result = run_db_query(sql, result=True)

    for j in result:
        jobs.append(j)


def commit_to_db(sessionID, result):
    for i in result:
        insert_into_table(
            "questions",
            ["questionID", "question", "answer", "wrongAnswers", "sessionID"],
            [gen_code(5), "asdfasdf", "asdfasdf", "asdfasdf", sessionID],
        )


processing = True

while True:
    if not processing:
        sleep(1)
        print("slow")

    processing = False
    check_for_jobs()

    if len(jobs) != 0:
        for count, j in enumerate(jobs):
            SessionID, text = j
            jobs.pop(count)
            print(SessionID)
            result = run_ml(text)
            commit_to_db(SessionID, result)
            processing = True
