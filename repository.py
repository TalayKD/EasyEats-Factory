import psycopg2

# Function to connect Flask app to the postgres database

def get_db_connection():
    conn = psycopg2.connect(
            host= 'ec2-34-252-216-149.eu-west-1.compute.amazonaws.com',
            database= 'dd2b432ofna5kk',
            user= 'knsfeqfqdhhygm',
            password= 'c2634a15369c268a94d4c8d1cf7da0e01d9b9da2bfa6da4c4ffb2a6b9de1f09d',
            port= 5432,
            sslmode='require'
    )
    return conn

def close_db_connection():
    cur.close()
    conn.close()
    print("Database connection closed! Safe to exit app")
    return "Database connection closed! Safe to exit app"

# Initialize connection and cursors

conn = get_db_connection()
cur = conn.cursor()

#####################
### Create tables ###
#####################

# Function to create user table
def create_client_table():
    try:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS client(
                client_id uuid NOT NULL, 
                name VARCHAR(50) NOT NULL,
                email VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50),
                PRIMARY KEY (client_id)
            );''')  
        conn.commit()
    except Exception as e:
        print("create client table ERROR : " , str(e))
        return "create client table ERROR : " + str(e)
    else:
        print("Client Table created successfully.")
        return "Client Table created successfully."


# Initialize table with one client
def init_client_table():
    try:
        cur.execute('''
            INSERT INTO client (name, email, password)
            VALUES ('Talay Kondhorn', 'talaykd@gmail.com', 'helloworld')
            ''') 
        conn.commit()
    except Exception as e:
        print("initialized client table ERROR : " , str(e))
        return "initialized client table ERROR " + str(e)
    else:
        print("Initialized client table successfully.")
        return "Initialized client table successfully."


def create_customer_table():
    try:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS customer (
                customer_id uuid NOT NULL,
                firstname varchar(50) NOT NULL,
                lastname varchar(50) NOT NULL,
                gender varchar(50) NOT NULL,
                email varchar(50) NOT NULL,
                phonenumber varchar(10),
                birthdate date NOT NULL,
                nationality varchar(50) NOT NULL,
                PRIMARY KEY (customer_id)
            );''')  
        conn.commit()
    except Exception as e:
        print("create customer table ERROR : " , str(e))
        return "create customer table ERROR : " + str(e)
    else:
        print("Customer Table created successfully.")
        return "Customer Table created successfully."


def create_restaurant_table():
    try:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS restaurant (
                restaurant_id uuid NOT NULL,
                restaurantname varchar(50) NOT NULL,
                cuisinetype varchar(100) NOT NULL,
                imageurl varchar(1000) NOT NULL,
                PRIMARY KEY (restaurant_id)
            );''')  
        conn.commit()
    except Exception as e:
        print("create restaurant table ERROR : " , str(e))
        return "create restaurant table ERROR : " + str(e)
    else:
        print("Restaurant Table created successfully.")
        return "Restaurant Table created successfully."


def create_branch_table():
    try:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS branch (
                branch_id uuid NOT NULL,
                branchname varchar(100) NOT NULL,
                restaurant_id uuid NOT NULL,
                location varchar(500) NOT NULL,
                numtable int NOT NULL,
                PRIMARY KEY (branch_id),
                FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id)
            );''')  
        conn.commit()
    except Exception as e:
        print("create branch table ERROR : " , str(e))
        return "create branch table ERROR : " + str(e)
    else:
        print("Branch Table created successfully.")
        return "Branch Table created successfully."


def create_order_table():
    try:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS myorder (
                myorder_id uuid NOT NULL,
                ordername varchar(100) NOT NULL,
                customer_id uuid NOT NULL,
                branch_id uuid NOT NULL,
                tablenumber int NOT NULL,
                ordertime timestamp NOT NULL,
                ordercompleted bool NOT NULL,
                PRIMARY KEY (myorder_id),
                FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
                FOREIGN KEY (branch_id) REFERENCES branch(branch_id)
            );''')  
        conn.commit()
    except Exception as e:
        print("create order table ERROR : " , str(e))
        return "create order table ERROR : " + str(e)
    else:
        print("Order Table created successfully.")
        return "Order Table created successfully."


def create_menuitem_table():
    try:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS menuitem (
                menuitem_id uuid NOT NULL,
                menucategory varchar(100) NOT NULL,
                restaurant_id uuid NOT NULL,
                menuitemname varchar(100) NOT NULL,
                customizableinstr varchar(1000),
                imageurl varchar(1000) NOT NULL,
                description varchar(1000),
                available boolean NOT NULL,
                PRIMARY KEY (menuitem_id),
                FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id)
            );''')  
        conn.commit()
    except Exception as e:
        print("create menu item table ERROR : " , str(e))
        return "create menu item table ERROR : " + str(e)
    else:
        print("MenuItem Table created successfully.")
        return "MenuItem Table created successfully."


def create_orderitem_table():
    try:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS orderitem (
                orderitem_id uuid NOT NULL,
                myorder_id uuid NOT NULL,
                branch_id uuid NOT NULL,
                menuitem_id uuid NOT NULL,
                quantity int NOT NULL,
                delivered bool NOT NULL,
                customizabletext varchar(1000),
                PRIMARY KEY (orderitem_id),
                FOREIGN KEY (myorder_id) REFERENCES myorder(myorder_id),
                FOREIGN KEY (menuitem_id) REFERENCES menuitem(menuitem_id),
                FOREIGN KEY (branch_id) REFERENCES branch(branch_id)
            );''')  
        conn.commit()
    except Exception as e:
        print("create order item table ERROR : " , str(e))
        return "create order item table ERROR : " + str(e)
    else:
        print("OrderItem Table created successfully.")
        return "OrderItem Table created successfully."


#####################
### Table Actions ###
#####################

# table is a string of table name
def get_table(table):
    order = "SELECT * from " + str(table) + " ORDER BY " + str(table) + "_id ASC"
    cur.execute(order)
    data = cur.fetchall()
    return data

# field is a string of field name
def get_table_col(table, field):
    order = "SELECT " + str(field) + " FROM " + str(table)
    cur.execute(order)
    data = cur.fetchall()
    return data

def get_table_row(table, col, value):
    order = "SELECT * from " + str(table) + " WHERE " + str(col) + "="
    if (isinstance(value, str)):
        order = order + "\'" + str(value) + "\'"
    else:
        order = order + str(value)
    cur.execute(order)
    data = cur.fetchall()
    return data
    

# table is a string of table name
# fields is an array of columns to be inserted into
# values is an array of the corresponding values in each column
def insert_row(table, fields, values):
    order = "INSERT INTO " + str(table) + "("
    for field in fields:
        order = order + str(field) + ','
    order = order[:-1] + ") VALUES("
    for value in values:
        if (isinstance(value, str)):
            order = order + "\'" + str(value) + "\'"
        else:
            order = order + str(value)
        order = order + ","
    order = order[:-1] + ")"
    # Connect to database and execute
    cur.execute(order)
    conn.commit()

# data is a dictionary that stores column : value pairs
# update only at row with val if the arguments are given
def update_table(table, data, col=None, row=None):
    order = "UPDATE " + str(table) + " SET"
    for d in data:
        #check if type is string
        if (isinstance(data[d], str)):
            order = order + " " + str(d) + " = " + "\'" + str(data[d]) + "\'"
        else:
            order = order + " " + str(d) + " = " + str(data[d])
        order = order + ","
    order = order[:-1]
    if (col != None):
        if (isinstance(row, str)):
            order = order + " WHERE " + str(col) + "=" + "\'" + str(row) + "\'"
        else:
            order = order + " WHERE " + str(col) + "=" + str(row)
    #connect to database
    cur.execute(order)
    conn.commit()

# delete only at col with row (value in col) only if arguments are given
# otherwise, delete all rows in the table
def delete_row(table, col=None, row=None):
    order = "DELETE  FROM " + str(table)
    if (col != None):
        if (isinstance(row, str)):
            order = order + " WHERE " + str(col) + "=" + "\'" + str(row) + "\'"
        else:
            order = order + " WHERE " + str(col) + "=" + str(row) 
    #Delete data from database
    cur.execute(order)
    conn.commit()
