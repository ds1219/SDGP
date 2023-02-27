import mysql.connector


def runDBQuery(query: str, val: tuple):
    mydb = mysql.connector.connect(
        host="localhost", user="backend", password="b3k3nd", database="sdgpTest"
    )
    cursor = mydb.cursor()
    cursor.execute(query, val)
    mydb.commit()
    cursor.close()
    mydb.close()


def checkForIDInTable(table: str, column: str, idString: str):
    query = f'SELECT * FROM `{table}` WHERE EXISTS(SELECT * From Lecturer WHERE %s LIKE "%s")'

    vals = (table, column, idString)
    return runDBQuery(query, vals)


def InsertIntoTable(table: str, values: list):

    query = f"INSERT INTO `{table}` (sessionID, lecturerID, sessionTime, sessionDate, subjectID) VALUES (%s, %s, %s, %s, %s);"

    runDBQuery(query, values)
