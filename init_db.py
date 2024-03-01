
import  psycopg2





def insertToDatabase(title, url):
    try:
        conn = psycopg2.connect(database='my_pgdb', user='postgres', password='anuj', host='localhost', port=5432)
        cur = conn.cursor()
        cur.execute("INSERT INTO images (title, url) VALUES (%s, %s)", (title, url))
        conn.commit()
    except psycopg2.Error as e:
        print("Error inserting into database:", e)
    finally:
        conn.close()


def getImagesFromDatabase():
    try:
        conn = psycopg2.connect(database='my_pgdb', user='postgres', password='anuj', host='localhost', port=5432)
        cur = conn.cursor()
        cur.execute("SELECT title, url FROM images")
        images = cur.fetchall()  # Fetch all rows from the query result
        return images
    except psycopg2.Error as e:
        print("Error fetching data from database:", e)
    finally:
        conn.close()