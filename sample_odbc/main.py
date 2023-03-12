import pyodbc

server = "localhost"
database = "psql"
user = "yuta_ushizima"
password = "0nly0ne0r@ngE"

cnn_postgres = pyodbc.connect('DRIVER=PostgreSQL;UID=' + user + ';PWD=' + password + ';DATABASE=' + database + ';SERVER=' + server + ';')
cursor = cnn_postgres.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()

cursor.close()
