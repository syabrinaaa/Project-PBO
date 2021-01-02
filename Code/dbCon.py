import mysql.connector

class MySql:
    def close():
        con.Close()

    def update(code, value):
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database = "synergasia"
            )
            cursor = con.cursor();
            cursor.execute(code, value)
            con.commit()
        except mysql.connector.Error as e:
            print("Failed connect to database in MySQL: {}".format(e))

    def read(code, value):
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database = "synergasia"
            )
            cursor = con.cursor();
            cursor.execute(code, value)
            data = []
            for i in cursor:
                data.append(i)
            return data
        except mysql.connector.Error as e:
            print("Failed connect to database in MySQL: {}".format(e))