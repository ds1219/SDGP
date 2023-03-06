import mysql.connector


def run_db_query(query: str, val: tuple):
    mydb = mysql.connector.connect(
        host="localhost", user="backend", password="b3k3nd", database="sdgpTest"
    )
    cursor = mydb.cursor()
    cursor.execute(query, val)

    mydb.commit()
    cursor.close()
    mydb.close()


def check_for_item_in_table(table: str, column: str, idString: str):
    query = f"SELECT * FROM `{table}` WHERE EXISTS(SELECT * From `{table}` WHERE {column} LIKE %s)"

    vals = (table, column, idString)
    return run_db_query(query, vals)


def insert_into_table(table: str, columns: list, values: list):
    columns = ", ".join(columns)

    query = f"INSERT INTO `{table}` ({columns}) VALUES (%s, %s, %s, %s, %s);"

    run_db_query(query, values)
