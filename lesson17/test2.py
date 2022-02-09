import mysql.connector


class Runner:

    def __init__(self):
        db_connect = mysql.connector.connect(
            database="mysql",
            host="localhost",
            user="jet_admin",
            passwd="123"
        )
        self.cursor = db_connect.cursor()
        self.get_command()
        self.cursor.close()

    def run_sql(self, sql_command):
        try:
            self.cursor.execute(sql_command)
        except mysql.connector.errors.ProgrammingError as error:
            print(error.msg)
        for db in self.cursor:
            print(str(db).replace('(', '').replace(')', ''))

    def get_command(self):
        while (value := input("Enter SQL > ")) != "exit":
            self.run_sql(value)
        print("Work with the database is complete")


if __name__ == "__main__":
    Runner()
