import mysql.connector


        
        
def connect_db():
    dict = {
        'database' : 'ecommerce_db', # type: ignore
        'user' : 'root', # type: ignore
        'password' : 'Renae5776', #type: ignore
        'host' : 'localhost' #type: ignore
    }

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

            
            