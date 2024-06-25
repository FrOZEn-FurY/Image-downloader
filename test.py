# This file is to test if the data written in the database is correct or not.
import psycopg2
import os

conn = psycopg2.connect(
    host="localhost",
    database="images",
    user="root",
    password="root1234",
    port="5432",
)
cur = conn.cursor()
cur.execute("SELECT image FROM imgs")
rows = cur.fetchall()
if not os.path.exists("Read"):
    os.mkdir("Read")
for index, row in enumerate(rows):
    with open(f"Read/pic{index}.png", "wb") as f:
        f.write(row[0])
cur.close()
conn.close()