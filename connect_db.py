import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

   
        
def connect_db():
    dict = {
        'database' : os.environ.get('DATABASE'), # type: ignore
        'user' : os.environ.get('USER'), # type: ignore
        'password' : os.environ.get('PASSWORD'), #type: ignore
        'host' : os.environ.get('HOST') #type: ignore
    }
    print(dict)

    try: 
        # attempt to establish a connection
        conn = mysql.connector.connect(**dict)
        
        # check for successful connection
        if conn.is_connected():
            print(f"You have successfully connect to {dict['database']}")
        
            return conn 
            
    except mysql.connector.Error as e:
        # catch any errors
        print(f"Error: {e}")

            
            