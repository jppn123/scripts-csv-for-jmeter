import csv
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

file = open("statistics.csv")
csvreader = csv.reader(file)
values = [val for val in csvreader]
data = {
    'sampler': [int(x[1]) for x in values[:-1]], 
    'average': [float(x[2]) for x in values[:-1]],
    'median': [float(x[3]) for x in values[:-1]],
    '90_line': [float(x[4]) for x in values[:-1]],
    '95_line': [float(x[5]) for x in values[:-1]],
    '99_line': [float(x[6]) for x in values[:-1]],
    'error_percent': [float(x[9][:-1]) for x in values[:-1]],
    'throughput': [float(x[10]) for x in values[:-1]]
}

db_url = 'postgresql://postgres:admin@localhost:5432/jmeter-csv-stats'
db = create_engine(db_url)
connection = db.connect()

df = pd.DataFrame(data)
df.to_sql('valores', con=connection, if_exists='replace', index=False)

conn = psycopg2.connect(db_url)
conn.autocommit = True

cursor = conn.cursor() 
  
sql1 = '''select * from valores;'''
cursor.execute(sql1) 
for i in cursor.fetchall(): 
    print(i) 
  
conn.commit() 
conn.close() 