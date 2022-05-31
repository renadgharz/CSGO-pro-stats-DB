import sqlalchemy, pymssql, pyodbc
from sqlalchemy import create_engine, text
from secrets import credentials as creds

username = creds.get('user')
password = creds.get('pwd')
host = creds.get('hostname')
port = creds.get('port')

conn_str = f'mssql+pymssql://{username}:{password}@{host}:{port}/Players'
engine = create_engine(conn_str)

