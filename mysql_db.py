import mysql.connector

dict = {
    'database' : 'ecommerce_db', # type: ignore
    'user' : 'root', # type: ignore
    'password' : 'Renae5776', #type: ignore
    'host' : 'localhost' #type: ignore
}
        
        
def customer_query():
   

    try: 
        # attempt to establish a connection
        conn = mysql.connector.connect(**dict)
        
        # check for successful connection
        if conn.is_connected():
            print(f"You have successfully connect to {dict['database']}")
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
        conn = mysql.connector.connect(**dict)
        
        # check for successful connection
        if conn.is_connected():
            print(f"You have successfully connect to {dict['database']}")
            
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
    
create_customer("Henri Swiggum", 'henris@gmail.com')  
customer_query()   
    