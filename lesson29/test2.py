import mysql.connector
import hashlib


def encrypt_pass(password):
    return hashlib.sha1(password.encode())


def update_db():
    db_connect = mysql.connector.connect(
        database=db_name,
        host="localhost",
        user="jet_admin",
        passwd="123"
    )
    db_connect.cursor().execute(f"USE {db_name}")
    db_connect.cursor().execute(f"INSERT INTO users (login, passwd) VALUES ('{login}', '{passwd.hexdigest()}')")
    db_connect.commit()
    db_connect.cursor().close()


if __name__ == "__main__":
    db_name = "example"
    login = input("Enter login: ")
    passwd = input("Enter password: ")
    if login and passwd:
        update_db(login, encrypt_pass(passwd))
        print(f"The database '{db_name}' is updated!")
    else:
        print("Login or password can't be empty values!")
