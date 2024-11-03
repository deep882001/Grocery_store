import mysql.connector

__cnx = None

def get_sql_connection():
    print("OPening mysql connection")
    global __cnx

    if __cnx is None: 
        __cnx = mysql.connector.connect(user='root', password='Pat48830$', database='Grocery_store')
    
    return __cnx