import mysql.connector


class DB:
    def __init__(self):
        # Database credentials
        self.host = "localhost"
        self.user = "root"
        self.password = "root"
        self.database = "Articles"
        self.connection = None

    def connect(self):
        # Establish the database connection
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to the database")
        except Exception as e:
            print("Error:", str(e))

    def close(self):
        # Close when needing to make changes to DB
        self.connection.close()
