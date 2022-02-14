import mysql.connector


class Runner:

    def __init__(self):
        self.database_name = "first"
        self.db_connect = self.connect_database()
        self.cursor = self.db_connect.cursor()
        self.change_db_data()
        self.show_db_data()

    def connect_database(self):
        db_connect = mysql.connector.connect(
            database="mysql",
            host="localhost",
            user="jet_admin",
            passwd="123"
        )
        return db_connect

    def change_db_data(self):
        self.cursor.execute(f"USE {self.database_name}")
        self.cursor.execute(f"DELETE FROM product WHERE id=2")
        self.cursor.execute(f"UPDATE product set price = '63 руб' WHERE name='молоко'")
        self.cursor.execute(f"UPDATE product set price = '34 руб' WHERE name='макароны'")
        self.cursor.execute(f"INSERT INTO product (name, price) VALUES ('мука ржаная', '54 руб')")
        self.cursor.execute("ALTER TABLE product ADD COLUMN IF NOT EXISTS note VARCHAR(30)")
        self.db_connect.commit()

    def show_db_data(self):
        self.cursor.execute(f"SELECT * FROM product")
        for db in self.cursor:
            print(str(db).replace('(', '').replace(')', ''))


if __name__ == "__main__":
    Runner()
