import mysql.connector
from connect_db import connect_db
        
        
def customer_query():
   

    try: 
        # attempt to establish a connection
        conn = connect_db()
        
        cursor = conn.cursor()
        
        # starting sql query to a variable
        query = "SELECT * FROM Customer"
        cursor.execute(query)
        customers = cursor.fetchall()
        
        for row in customers:
            print(row)
            
            
    except mysql.connector.Error as e:
        # catch any errors
        print(f"Error: {e}")

    finally:
        # close the connection
        if conn and conn.is_connected():
            conn.close()
            print("MySQL connection closed")
            

def create_customer(*customer):


    try: 
        # attempt to establish a connection
        conn = connect_db()
        
       
            
        query = "INSERT INTO Customer (name, email) VALUES(%s, %s)"
        
        cursor = conn.cursor()
        cursor.execute(query, customer)
        conn.commit()
        
        print(f"New Customer was successfully added")
            
            
    except mysql.connector.Error as e:
        # catch any errors
        print(f"Error: {e}")

    finally:
        # close the connection
        if conn and conn.is_connected():
            conn.close()
            print("MySQL connection closed")
    
create_customer("Boba Fett", 'bbfett@gmail.com')  
customer_query()   
    