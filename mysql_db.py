import mysql.connector



db_name = 'ecommerce_db'
user = 'alexs'
password = 'alex'
host = '127.0.0.1'

try: 
    # attempt to establish a connection
    conn = mysql.connector.connect(
        dabase = db_name,
        user = user,
        password = password,
        host = host
    )
    
    # check for successful connection
    if conn.is_connected():
        print(f"You have successfully connect to {db_name}")
        
except mysql.connector.Error as e:
    # catch any errors
    print(f"Error: {e}")

finally:
    # close the connection
    if conn and conn.is_connected():
        conn.close()
        print("MySQL connection closed")
    