import mysql.connector


def dataConnect(): 
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database="adsi_tarde_python"    
    )
    cursor = database.cursor(buffered=True)
    return [database, cursor]
