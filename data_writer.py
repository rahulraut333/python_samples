"""
purpose of this module is to read data from json files and save it into postgresql database.
"""
import json
import psycopg2

def connect_db_conn(user="postgres", password="postgres", host="localhost", port="5432", database="postgres"):
    """
    creates connection to postgresql using pg configurations.
    """    
    connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
    cursor = connection.cursor()
    return cursor, connection

def add_data(cursor, connection, record):
    """
    runs raw insert query to insert data into table.
    """
    try:
       postgres_insert_query = """ INSERT INTO employee (id, employee_name, employee_salary, employee_age, profile_image) VALUES (%s,%s,%s,%s,%s)"""
       cursor.execute(postgres_insert_query, record)
       connection.commit()
       count = cursor.rowcount
       print (count, "Record inserted successfully into employee table")

    except (Exception, psycopg2.Error) as error :
        print("Failed to insert record into employee table", error)
        raise

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def read_data(filename):
    """
    reads json file and saves data into database
    """
    cur, connection = connect_db_conn()
    with open(filename) as fp:
        rec = json.load(fp)
        add_data(cur, connection, tuple(rec.values()))
        print("ADDED DATA")

read_data(r"F:\rahul\demo\json_store\2.json")
