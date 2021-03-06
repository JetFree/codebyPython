import hashlib

import mysql.connector


class Db_manager:

    def __init__(self):
        self.db_connect = mysql.connector.connect(
            database=db_name,
            host="localhost",
            user="jet_admin",
            passwd="123"
        )
        self.cursor = self.db_connect.cursor()
        self.cursor.execute(f"USE {db_name}")

    def is_login_exist(self, username):
        self.cursor.execute(f"SELECT * FROM users WHERE login='{username}'")
        result = self.cursor.fetchone()
        return result is not None

    def verify_password(self, login, password):
        self.cursor.execute(f"SELECT passwd from users WHERE login='{login}'")
        result = self.cursor.fetchone()
        if hashlib.sha1(password.encode()).hexdigest() == result[0]:
            print("Access is opened!")
        else:
            print("Access is denied!")


if __name__ == "__main__":
    db_name = "example"
    if login := input("Enter login: "):

        if (db_mng := Db_manager()).is_login_exist(login):
            passwd = input("Enter password: ")
            db_mng.verify_password(login, passwd)
        else:
            print("Access is denied!")
    else:
        print("Login or password can't be empty values!")
