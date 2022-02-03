import mysql.connector


if __name__ == "__main__":
    mydb = mysql.connector.connect(
        database="mysql",
        host="localhost",
        user="jet_admin",
        passwd="123"
    )
    database_name = "first"
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE first")
    mycursor.execute("USE first")
    mycursor.execute("CREATE TABLE product (id INT AUTO_INCREMENT PRIMARY KEY,"
                     "name VARCHAR(255),"
                     "price VARCHAR(255))")
    ins_tab = "INSERT INTO product (name, price) VALUES (%s, %s)"
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
    mycursor.executemany(ins_tab, val)
    mydb.commit()
    mydb.close()
    print(f"The database '{database_name}' was created!")