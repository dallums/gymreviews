import mysql.connector

class DataBase:
    def get_connection():
        return mysql.connector.connect(
                host="localhost",
                user="yourusername",
                password="yourpassword",
                database="yourdatabase"
                )