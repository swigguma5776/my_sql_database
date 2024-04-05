from connect_db import connect_db


def update_customer(*customer):
    conn =  connect_db()
    try:
        cursor = conn.cursor()
        
        
        query = f"UPDATE Customer SET name = %s WHERE customer_id = %s"
        
        cursor.execute(query, customer)
        conn.commit()
        
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Successfully updated Customer")
        cursor.close()
        conn.close()
        
update_customer('Obi Wan', 6)