# Use Python to Query SQL DB and Create CSV/Excel Files
There are a few ways to use the code but for now I will create a python file which will simply intake your SQL DB hostname, port, and SQL query. Ideally once your have your query working you can imporve on it and create more functions based off your company needs

### Imported Modules

- shutil - helps automate copying files and directories (https://docs.python.org/3/library/shutil.html)
- openpyxl - Allows you edit excel files (https://openpyxl.readthedocs.io/en/stable/)
- csv - Allows you to edit CSV files (https://docs.python.org/3/library/csv.html)
- boto3 - Mostly use to levearge APIs calls in your AWS Account, does require AWS CLI to in order to configure Access and Secret Keys (https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

### Installing Requirements and How to use the script

To run the script, you will need to have Python 3.6+ installed.  
Dependencies are listed in **requirements.txt**. You can install them using:  
```
pip3 install -r requirements.txt
```

Once the requirements are installed you will need to update main.py and reference the function example_sql_query(). This function has a example of how to use pymysql and you enter your own SQL command based of your database tables. I will create a python task with screen shots in the examples folder leverage a RDS database in AWS. 


### How can this help with day-to-day tasks

- Use the script to query SQL DB and use that data to run other functions
- Use the script to query SQL DB, save the data to a excel or csv  file, and place file in S3 bucket or email (if no PII data is in :) )
- As a network engineer I used a RDS Database Server which contained IPs, Default Gateway, hostnames, Crypto Keys for 8 VPN tunnels, etc and generated a running configuration file based off a template (basically a find and replace using SQL variables) 

### TIPS!!!!

Security is very important I'm going to use AWS Secrets Manager to store my Database hostname, username, and passwords. You should never store any kind of username/passwords in your code and should leverage something like a Secrets Manager or Vault which you will make a API call against to fetch username/passwords and it should be limited to a specific IP range or AWS account for added layer of security.

AWS Secret Manager is very easy to setup and is free to use and they will provide the code for you to use APIs to contact to the Secrets Manager in that region (note this will require assume-role and other AWS security features to work)

<!--- ![](https://github.com/pyjoepy06/sql_python_query/blob/main/docs/aws_secrets_manager.GIF) --->

<!--- img src="https://github.com/pyjoepy06/sql_python_query/blob/main/docs/aws_secrets_manager.GIF" width="20000" height="400" /> --->