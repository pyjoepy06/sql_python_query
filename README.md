# Use Python to Query SQL DB and Create CSV/Excel Files
There are a few ways to use the code but for now I will create a python file which will simply intake your SQL DB hostname, port, and SQL query. Ideally once your have your query working you can imporve on it and create more functions based off your company needs

### How to use the script

### How can this help with day-to-day tasks

- Use the script to query SQL DB and use that data to run other functions
- Use the script to query SQL DB, save the data to a excel or csv  file, and place file in S3 bucket or email (if no PII data is in :) )
- As a network engineer I used a RDS Database Server which contained IPs, Default Gateway, hostnames, Crypto Keys for 8 VPN tunnels, etc and generated a running configuration file based off a template (basically a find and replace using SQL variables) 

### TIPS!!!!

Security is very important I'm going to use AWS Secrets Manager to store my Database hostname, username, and passwords. You should never store any kind of username/passwords in your code and should leverage something like a Secrets Manager or Vault which you will make a API call against to fetch username/passwords and it should be limited to a specific IP range or AWS account for added layer of security.

AWS Secret Manager is very easy to setup and is free to use and they will provide the code for you to use APIs to contact to the Secrets Manager in that region (note this will require assume-role and other AWS security features to work)

![Alt Text](https://github.com/pyjoepy06/sql_python_query/blob/main/docs/aws_secrets_manager.GIF)