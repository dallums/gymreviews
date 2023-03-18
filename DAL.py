import mysql.connector

class DataBase:
    def get_connection(self):
        return mysql.connector.connect(
                host="localhost",
                user="test",
                password="mypassword",
                database="gymreviews"
                )