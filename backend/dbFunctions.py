import mysql.connector


def runDBQuery(query: str, val: list):
    with mysql.connector.connect(
        host="127.0.0.1", user="root", password="", database="sdgpTest"
    ) as myDB:
        myCursor = myDB.cursor()
        myCursor.execute(query, val)


def checkForIDInTable(table: str, column: str, idString: str):
    query = f'SELECT * FROM `{table}` WHERE EXISTS(SELECT * From Lecturer WHERE %s LIKE "%s")'

    vals = (table, column, idString)
    return runDBQuery(query, vals)


def InsertIntoTable(table: str, values: list):

    query = f"INSERT INTO `{table}` (sessionID, lecturerID, sessionTime, sessionDate, subjectID) VALUES (%s, %s, %s, %s, %s);"

    runDBQuery(query, values)
