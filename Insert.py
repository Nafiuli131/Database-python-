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
insert_query = "INSERT INTO office(id, name) VALUES (1, 'Google'), (2,'Apple'), (3,'Microsoft')," \
               "(4,'Samsung') ,(5, 'Amazon'), (6, 'Samsaung'),(7, 'Nokia') , (8, 'Mi'), " \
               "(9, 'Vivo') , (10, 'One plus')"




cur.execute(insert_query)
conn.commit()

conn.close()
