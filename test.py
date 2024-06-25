# This file is to test if the data written in the database is correct or not.
import psycopg2
import os

conn = psycopg2.connect( # Database connection
    host="localhost",
    database="images",
    user="root",
    password="root1234",
    port="5432",
)
cur = conn.cursor()
cur.execute("SELECT image FROM imgs") # Selecting all the images (The binary data)
rows = cur.fetchall()
if not os.path.exists("Read"): # Making the needed path if not exists.
    os.mkdir("Read")
for index, row in enumerate(rows):
    with open(f"Read/pic{index}.png", "wb") as f: # Writing the data given from the database to a file.
        f.write(row[0])
cur.close()
conn.close()