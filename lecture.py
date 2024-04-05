import mysql.connector



db_name = 'ecommerce_db'
user = 'alexs'
password = 'alex'
host = '127.0.0.1'

try: 
    conn = mysql.connector.connect(
        dabase = db_name,
        user = user,
        password = password,
        host = host
    )
    
    if conn.is_connected():
        print(f"You have successfully connect to {db_name}")
        
except:
    