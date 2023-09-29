import pandas as pd
from Thesis.Data.Database import DB


class Handler:
    def __init__(self):
        self.database = DB()
        self.connect()

    # Open a connection to the database
    def connect(self):
        self.database.connect()

    def close(self):
        self.database.close()

    # region Stored Procedures

    def count_author(self):
        # Assuming you have a stored procedure named "sp_example" that takes no parameters
        procedure_name = "spCountAuthor"

        try:
            cursor = self.database.connection.cursor()
            cursor.callproc(procedure_name)
            results = list(cursor.stored_results())[0]
            cursor.close()
            self.database.connection.commit()

            df = pd.DataFrame(results.fetchall(), columns=[desc[0] for desc in results.description])
            print(df)
        except Exception as e:
            print("Error:", str(e))

    # endregion
    def summary(self):
        # This function will provide a summary of the datapoints I want to see.
        print("TODO")
