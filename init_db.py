
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

def Get_comapre_images():
    try:
        conn = psycopg2.connect(database='my_pgdb', user='postgres', password='anuj', host='localhost', port=5432)
        cur = conn.cursor()
        cur2 = conn.cursor()
        cur.execute("SELECT * FROM images order by vote desc limit 5")
        topFiveImages = cur.fetchall()
        cur2.execute("SELECT * FROM images WHERE id NOT IN ( SELECT id FROM images ORDER BY vote DESC LIMIT 5 ) ORDER BY vote DESC LIMIT 10")
        topMediumImages = cur2.fetchall()
        return {
            "topFive": topFiveImages,
            "medium": topMediumImages
        }

    except psycopg2.Error as e:
        print("Error inserting into database:", e)
    finally:
        conn.close()

def getImagesFromDatabase():
    try:
        conn = psycopg2.connect(database='my_pgdb', user='postgres', password='anuj', host='localhost', port=5432)
        cur = conn.cursor()
        cur.execute("SELECT title, url, vote FROM images order by vote desc limit 5;")
        images = cur.fetchall()  # Fetch all rows from the query result
        return images
    except psycopg2.Error as e:
        print("Error fetching data from database:", e)
    finally:
        conn.close()

def handleImageVote(selectedId, remainingId):
    try:
        conn = psycopg2.connect(database='my_pgdb', user='postgres', password='anuj', host='localhost', port=5432)
        cur = conn.cursor()

        # Get vote counts for selected and remaining IDs
        cur.execute("SELECT vote FROM images WHERE id = %s", (selectedId,))
        selectedVote = cur.fetchone()[0]  # Fetch and extract vote count
        print(selectedVote)
        cur.execute("SELECT vote FROM images WHERE id = %s", (remainingId,))
        remainingVote = cur.fetchone()[0]  # Fetch and extract vote count
        print(remainingVote)
        # Increment vote count for selected ID and decrement for remaining ID
        cur.execute("UPDATE images SET vote = %s WHERE id = %s", (selectedVote + 1, selectedId))
        cur.execute("UPDATE images SET vote = %s WHERE id = %s", (remainingVote - 1, remainingId))

        conn.commit()
        print("Votes updated successfully.")
    except psycopg2.Error as e:
        print("Error updating votes:", e)
    finally:
        conn.close()
