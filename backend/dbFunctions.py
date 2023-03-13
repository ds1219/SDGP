import mysql.connector


def run_db_query(query: str, val: tuple, result=False):
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="", database="sdgptest"
    )
    cursor = mydb.cursor()
    cursor.execute(query, val)

    if result == False:
        mydb.commit()

    queryResult = cursor.fetchall()
    cursor.close
    mydb.close()

    if result:
        return queryResult


def check_for_item_in_table(table: str, column: str, idString: str):
    query = f"SELECT * FROM `{table}` WHERE EXISTS(SELECT * From `{table}` WHERE {column} LIKE %s)"

    vals = (idString,)
    result = run_db_query(query, vals, result=True)

    return len(result) != 0


def insert_into_table(table: str, columns: list, values: list):
    columns = ", ".join(columns)

    query = f"INSERT INTO `{table}` ({columns}) VALUES ({('%s,'*len(values))[:-1]});"
    print(query)

    run_db_query(query, values)
