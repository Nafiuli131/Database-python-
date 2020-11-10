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
CREATE TABLE Office(
    id integer PRIMARY KEY,
    name text

)
""")
conn.commit()
print("Table create Successfully")
