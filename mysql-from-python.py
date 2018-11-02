import os
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

#connect to the dgiyatabase
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
try:
    # Run a query
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'),
                (24, "Jim"),
                (25, "Fred")]
        cursor.executemany("UPDATE Friends SET age= %s WHERE name= %s;",rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
