from connect_db import connect_db
        
            

def create_customer(*customer):


    # attempt to establish a connection
    conn = connect_db()
    
    try: 
        
    
            
        query = "INSERT INTO Customer (name, email) VALUES(%s, %s)"
        
        cursor = conn.cursor()
        cursor.execute(query, customer)
        conn.commit()
        
        print(f"New Customer was successfully added")
            
            
    except Exception as e:
        # catch any errors
        print(f"Error: {e}")

    finally:
        # close the connection
        if conn and conn.is_connected():
            conn.close()
            print("MySQL connection closed")
    
create_customer("Boba Fett", 'bbfett@gmail.com')  
 
    