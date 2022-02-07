import mysql.connector

val = [
    ("батон нарезной", "21 руб"),
    ("масло подсолнечное", "60 руб"),
    ("крупа гречневая", "80 руб"),
    ("молоко", "54 руб"),
    ("яйцо куриное", "55 руб"),
    ("кетчуп", "75 руб"),
    ("сок томатный", "92 руб"),
    ("макароны", "30 руб"),
    ("зелёный корошек", "45 руб"),
    ("селёдка", "150 руб"),
]
database_name = "first"
db_connect = None


def connect_database():
    global db_connect
    db_connect = mysql.connector.connect(
        database="mysql",
        host="localhost",
        user="jet_admin",
        passwd="123"
    )


def create_data():
    mycursor = db_connect.cursor();
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    mycursor.execute(f"USE {database_name}")
    mycursor.execute("CREATE TABLE IF NOT EXISTS product (id INT AUTO_INCREMENT PRIMARY KEY,"
                     "name VARCHAR(255),"
                     "price VARCHAR(255))")
    ins_tab = "INSERT INTO product (name, price) VALUES (%s, %s)"

    mycursor.executemany(ins_tab, val)
    db_connect.commit()
    print(f"The database '{database_name}' was created!")


if __name__ == "__main__":
    connect_database()
    create_data()
    db_connect.close()
