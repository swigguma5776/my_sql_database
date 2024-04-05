from connect_db import connect_db


def fetch_customers():
   
    # attempt to establish a connection
    conn = connect_db()
    
    try: 
        
        cursor = conn.cursor()
        
        # starting sql query to a variable
        query = "SELECT * FROM Customer"
        cursor.execute(query)
        customers = cursor.fetchall()
        
        for row in customers:
            print(row)
            
            
    except Exception as e:
        # catch any errors
        print(f"Error: {e}")

    finally:
        # close the connection
        if conn and conn.is_connected():
            conn.close()
            print("MySQL connection closed")
            
fetch_customers()