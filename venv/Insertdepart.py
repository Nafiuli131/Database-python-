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
insert_query ="INSERT INTO department (d_id,name, office_id) VALUES (1,'g','ECE'),(1,'fgf','ME')," \
              "(1,'g','mn'),(1,'g34','EeeE'),(1,'eriy','sdsE'),(10,'ger','eeqECE')"

cur.execute(insert_query)
conn.commit()

conn.close()

#d_names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]

#query = "INSERT INTO department (d_id,name, office_id) VALUES " \
        #+ ", ".join(map(str, map(lambda t: (t[0] + 1, t[1], (t[0] % 10) + 1), enumerate(d_names))))

#print(query)
