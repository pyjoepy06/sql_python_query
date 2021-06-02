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


def example_sql_query(hostname,username,password,db_name,port_number):
    """This is a example function which will query * in a specific table"""
    #Create a empty list of data
    sql_data = []
    
    #creating connection to the database
    connection = db_connection(hostname,username,password,db_name,port_number)
    
    #Setting the cursor
    cursor = connection.cursor()
    
    #Execute the SQL Query using execute() method, replace db_table_here with your db_table #
    #Or SELECT specific columns 
    #Or add your specific SQL query
    #Or pass in variables of your own
    
    cursor.execute ("""SELECT * FROM db_table_here""")
    
    #fetching all records
    
    data = cursor.fetchall()
    return sorted(sql_data)

def csv_report_creator(sql_data):
    #Creates a csv file with all your data

    with open('my_report.csv', 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        #Add the header/column names
        header = ['make', 'style', 'color', 'plate']
        writer.writerow(header)
        
        #Iterate over data and write to the csv file
        
        for row in sql_data:
            writer.writerow(row)

def main():
    #print('This is example script using a already created SQL Database\n\n')
    username = input('Please enter your username for your Database: ')
    password = getpass(prompt='Database Password: ')
    db_name = input('Database DNS Name: ')
    port_number = input ('Database Port number (1521 or 3306 or custom number): ')
    
    #convert port_number into integer
    port_number = int(port_number)
    
    # Executing Example Jobs
    sql_query_job = example_sql_query(hostname,username,password,db_name,port_number)
    
    #Creating CSV File
    csv_report_creator(sql_query_job)