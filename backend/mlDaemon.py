from dbFunctions import *
from helperFunctions import gen_code
from time import sleep
from questionGenerator import getQAs


jobs = []


def check_for_jobs():
    sql = "SELECT sessionID, questionSource FROM lectureSessions WHERE sessionID NOT IN (SELECT sessionID FROM questions);"
    result = run_db_query(sql, result=True)

    for j in result:
        jobs.append(j)


def commit_to_db(sessionID, q, a, wa):
    insert_into_table(
        "questions",
        ["questionID", "question", "answer", "wrongAnswers", "sessionID"],
        [gen_code(5), q, a, wa, sessionID],
    )


processing = True

while True:
    if not processing:
        sleep(10)

    processing = False
    check_for_jobs()

    if len(jobs) != 0:
        for count, j in enumerate(jobs):
            SessionID, text = j
            jobs.pop(count)
            print(SessionID)

            from questionGenerator import getQAs

            result = getQAs(text)

            for i in result:
                q, a, wa = i
                commit_to_db(SessionID, q, a, wa)
            processing = True
