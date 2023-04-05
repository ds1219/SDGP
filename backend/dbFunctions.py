import mysql.connector


def run_db_query(query: str, val=False, result=False):
    """
    Executes the provided sql query

            Parameters:
                    query (str): The Query to be executed
                    val (tuple): values to be executed in the query
                    result (bool): switch to see if the query has return values

            Returns:
                    queryResult (list): The result of the query, if any
    """
    mydb = mysql.connector.connect(
        host="127.0.0.1", user="testuser", password="testpassword", database="sdgptest"
    )
    cursor = mydb.cursor()

    if val == False:
        cursor.execute(query, val)
    else:
        cursor.execute(query, val)

    if result == False:
        mydb.commit()

    queryResult = cursor.fetchall()
    cursor.close
    mydb.close()

    if result:
        return queryResult


def get_row_from_table(table: str, column: str, idString: str, multiple=False):
    query = f"SELECT * FROM `{table}` WHERE {column} LIKE %s;"
    vals = (idString,)
    result = run_db_query(query, vals, result=True)

    if len(result) == 0:
        print("[SERVER] - No Row Matching Query")
        raise ValueError

    if not multiple and len(result) > 1:
        print("[SERVER] - More than one row returned")
        raise ValueError

    return result


def insert_into_table(table: str, columns: list, values: list):
    columns = ", ".join(columns)

    query = f"INSERT INTO `{table}` ({columns}) VALUES ({('%s,'*len(values))[:-1]});"

    run_db_query(query, values)


def get_random_question_from_db(lectureSessionID: str):

    query = "SELECT * FROM questions Where `sessionID` LIKE %s ORDER BY RAND() LIMIT 1"
    vals = (lectureSessionID,)
    result = run_db_query(query, vals, result=True)

    if len(result) == 0:
        print("[SERVER] - No Row Matching Query")
        raise ValueError

    if len(result) > 1:
        print("[SERVER] - More than one row returned")
        raise ValueError

    return result
