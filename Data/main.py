import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

cursor = db.cursor()



def create_db():
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    print(f"Database {db_name} created!")
    cursor.execute(f"USE {db_name}")


def create_tables():
    cursor.execute(f"CREATE TABLE {table} (id INT AUTO_INCREMENT PRIMARY KEY, {column_1} VARCHAR(255), {column_2} VARCHAR(255))")
    print(f"Table {table} created!")


def create_rows():
    insert_data = f"INSERT INTO {table} ({column_1}, {column_2}) VALUES (%s, %s)"
    values = (row_1, row_2)
    cursor.execute(insert_data, values)
    db.commit()
    print(f"Data are insert in table {table}")




db_name = input("Enter a name of the database: ")
create_db()

table = input("Enter a name of the Table: ")
column_1 = input("Enter a name of the Column 1: ")
column_2 = input("Enter a name of the Column 2: ")
create_tables()

row_1 = input(f"Insert data in {column_1}: ")
row_2 = input(f"Insert data in {column_2}: ")
create_rows()
