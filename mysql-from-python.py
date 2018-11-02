import os
import datetime
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
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                       Friends(name char(20), age int, DOB datetime);""")
        # Note that the abpve will still display a warning (not error) if the
        # table already exists
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
