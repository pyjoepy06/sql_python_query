import boto3
import shutil
import openpyxl
import pymysql
from getpass import getpass
import csv

#Pymysql Function
def db_connection(hostname,username,password,db_name,port_number):
    """Connects to SQL DB using pymysql module and return the connection """
    connection = pymysql.connect(host=hostname, user=username, passwd=password, db=db_name, port=port_number)
    return(connection)


def cars_example_sql_query(hostname,username,password,db_name,port_number):
    """This is a example function which will query * in a specific table"""
    sql_data = []
    connection = db_connection(hostname,username,password,db_name,port_number)
    cursor = connection.cursor()
    cursor.execute ("""SELECT * FROM Cars""")
    sql_data = cursor.fetchall()
    return sorted(sql_data)

def persons_example_sql_query(hostname,username,password,db_name,port_number):
    """This is a example function which will query * in a specific table"""
    sql_data = []
    connection = db_connection(hostname,username,password,db_name,port_number)
    cursor = connection.cursor()
    cursor.execute ("""SELECT * FROM Persons""")
    sql_data = cursor.fetchall()
    return sorted(sql_data)

def specific_query_persons_example_sql_query(hostname,username,password,db_name,port_number):
    """This is a example function which will query * in a specific table"""
    sql_data = []
    connection = db_connection(hostname,username,password,db_name,port_number)
    cursor = connection.cursor()
    cursor.execute ("""SELECT PersonID, LastName, City FROM Persons WHERE PersonID=1""")
    sql_data = cursor.fetchall()
    return sorted(sql_data)


def cars_csv_report_creator(sql_data):
    with open('cars_report.csv', 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        header = ['make', 'model', 'year', 'location', 'available']
        writer.writerow(header)
        for row in sql_data:
            writer.writerow(row)

def persons_csv_report_creator(sql_data):
    with open('persons_report.csv', 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        header = ['person_id', 'FirstName', 'LastName', 'Address', 'City']
        writer.writerow(header)
        for row in sql_data:
            writer.writerow(row)

def specific_query_persons_csv_report_creator(sql_data):
    with open('persons_report.csv', 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        header = ['Person_id', 'LastName', 'City']
        writer.writerow(header)
        for row in sql_data:
            writer.writerow(row)

def main():
    #print('This is example script using a already created SQL Database\n\n')
    username = input('Please enter your username for your Database: ')
    password = getpass(prompt='Database Password: ')
    hostname = input('Please enter Database IP or  hostname: ')
    db_name = input('Database Name (my example: testDB): ')
    port_number = input ('Database Port number (1521 or 3306 or custom number): ')

    #convert port_number into integer
    port_number = int(port_number)

    # Executing Example Jobs
    sql_query_job = example_sql_query(hostname,username,password,db_name,port_number)

    #Creating CSV File
    csv_report_creator(sql_query_job)