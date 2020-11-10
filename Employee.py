import csv

import psycopg2

DB_NAME = "kfkpikep"
DB_USER = "kfkpikep"
DB_PASS = "xAc2rJe2Jxvg-ytrS6e6Twg7gNFpl60s"
DB_HOST = "lallah.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                        host=DB_HOST, port=DB_PORT)

print("Database create Successfully")


cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Employee(
    id integer PRIMARY KEY,
    name text,
    department_id integer,
    reporting_boss_id integer,
    joining_date DATE,
    leaving_date DATE,
    FOREIGN KEY(department_id) REFERENCES Department (d_id)
    
)
""")

with open('new_records.csv', 'r') as f:
    reader = csv.reader(f)
    i = 0
    next(reader)
    for row in reader:
        i += 1
        if i >20:
            break
        row = row[:5]
        cur.execute(
        "INSERT INTO Employee (id,name,joining_date,leaving_date,department_id) VALUES (%s,%s,%s,%s,%s)",
        row)
cur.close()
conn.commit()
print("Table create Successfully")
