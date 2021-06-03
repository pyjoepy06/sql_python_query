# Example of How to use the code for pymysql with AWS RDS Server

I have created a RDS server in Amazon which has a database name: testDB and is using the following Tables

![RDS_testDB_Tables](../docs/Database_Screenshot.jpg?raw=true "RDS testDB Database Tables")

### The example_main.py functions and how it works 

I created three functions for querying the testdb tables with a SELECT * FROM table_name and adding my own custom SQL Query the functions are named:

- cars_example_sql_query(hostname,username,password,db_name,port_number) **SQL Command: "SELECT * FROM Cars"**
- persons_example_sql_query(hostname,username,password,db_name,port_number) **SQL Commnad: "SELECT * FROM Persons"**
- specific_query_persons_example_sql_query(hostname,username,password,db_name,port_number) **SQL Command: "SELECT PersonID, LastName, City FROM Persons WHERE PersonID=1"**

I also created three CSV formats for each query:

- cars_csv_report_creator(sql_data) **Creates File name: cars_report.csv with custom headers**
- persons_csv_report_creator(sql_data) **Creates File name: persons_report.csv with custom headers**
- specific_query_persons_csv_report_creator(sql_data) **Creates File name: custom_persons_report.csv with custom headers**

Simply run the function with a assigned variable and then pass the variable to csv creator and your data is saved in a file locally where you executed the code. Next steps store in a s3 bucket, email to clients, or keep improving on the code for your own use