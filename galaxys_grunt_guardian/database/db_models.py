from database import db_connection

connection = db_connection.connect_to_database()

def verify_user(username, password): 
    
    sql = "SELECT * FROM players WHERE username = %s AND password = %s"
        
    db_connection.fetch_data(sql, (username, password))
        
    connection.commit()
    cursor = connection.cursor()

    if cursor.fetchone():
        return True
    else:
        return False