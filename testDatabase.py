import pymysql
import pymysql.cursors

# Replace these with your database connection info
host = "localhost"
user = "root"  # or your database user
password = "root"  # the password you used for the MySQL container
database = "Students"  # your database name

# Create a connection to the database
conn = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    cursorclass=pymysql.cursors.DictCursor
)

def selectAll(cursor):
    cursor.execute("SELECT * FROM student")

    records = cursor.fetchall()
    for record in records:
        print(record)

try:
    with conn.cursor() as cursor:
        selectAll(cursor)
        print("\n")
        
        sql2 = "INSERT INTO student (FirstName, LastName) VALUES (\"Test First\", \"Test Last\");"
        cursor.execute(sql2)

        ## Commit transaction
        conn.commit()

        selectAll(cursor)
        print("\n")


finally:
    # Close the connection
    conn.close()
