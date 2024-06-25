import psycopg2
import os

async def storeImages(path):
    try:
        conn = psycopg2.connect( # Database connection
        host="localhost",
        database="images",
        user="root",
        password="root1234",
        port="5432",
    )
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS imgs (id serial PRIMARY KEY, image bytea, path varchar(255))") # Creating the table if does not exists.
        for root, dirs, files in os.walk(path): # Walking on the content of the path
            for file in files:
                if file.endswith(".png") or file.endswith(".jpg"):
                    with open(os.path.join(root, file), "rb") as f:
                        cur.execute("INSERT INTO imgs (image, path) VALUES (%s, %s)", (psycopg2.Binary(f.read()), os.path.join(root, file))) # Storing the data of each image
                os.remove(os.path.join(root, file)) # Removing the image after storing it in the database
        conn.commit()
        cur.close()
        conn.close()
        print("Images stored successfully!")
    except psycopg2.Error as e:
        print(f"Error: {e}")