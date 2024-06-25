import psycopg2
import os

async def storeImages(path):
    try:
        conn = psycopg2.connect(
        host="localhost",
        database="images",
        user="root",
        password="root1234",
        port="5432",
    )
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS imgs (id serial PRIMARY KEY, image bytea, path varchar(255))")
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".png"):
                    with open(os.path.join(root, file), "rb") as f:
                        cur.execute("INSERT INTO imgs (image, path) VALUES (%s, %s)", (psycopg2.Binary(f.read()), os.path.join(root, file)))
                os.remove(os.path.join(root, file))
        conn.commit()
        cur.close()
        conn.close()
        print("Images stored successfully!")
    except psycopg2.Error as e:
        print(f"Error: {e}")