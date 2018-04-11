import pandas as pd
from sqlalchemy import create_engine

def getData():
  # Parameters
  ServerName = "ServerName"
  Database = "DatabaseName"
  UserPwd = "User:Password"
  Driver = "driver=SQL Server"

  # Create the connection
  engine = create_engine('mssql+pyodbc://' + UserPwd + '@' + ServerName + '/' + Database + "?" + Driver)

  sql = "select * from myTable"
  df = pd.read_sql(sql, engine)
  return df
df = getData()

# Write to SQL
# Parameters
# ServerName = "ServerName"
# Database = "DatabaseName"
# UserPwd = "UserName:Password"
# Driver = "driver=SQL Server" #driverName

# Create the connection
# engine = create_engine('mssql+pyodbc://' + UserPwd + '@' + ServerName + '/' + Database + "?" + Driver)

# sql = "select * mytable"
# df.to_sql("testing", engine)
