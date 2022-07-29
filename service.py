import repository
import uuid

from wtforms import Form, StringField, EmailField, PasswordField, validators
from wtforms.validators import ValidationError

########################################
### Database Initialization Services ###
########################################

clientCols = ["client_id", "name", "email", "password"]
customerCols = ["customer_id", "firstname", "lastname", "gender", "email", "phonenumber", "birthdate", "nationality"]
restaurantCols = ["restaurant_id", "restaurantname", "cuisinetype"]
branchCols = ["branch_id", "branchname", "restaurant_id", "location"]
myorderCols = ["myorder_id", "customer_id", "tablenumber", "ordertime", "ordercompleted"]
menuitemCols = ["menuitem_id", "menucategory", "restaurant_id", "menuitemname", "customizableinstr"]
orderitemCols = ["orderitem_id", "myorder_id", "menuitem_id", "quantity", "delivered", "customizabletext"]

def createClientTable():
    return repository.create_client_table()

def initClientTable():
    return repository.init_client_table()

def createCustomerTable():
    return repository.create_customer_table()

def createRestaurantTable():
    return repository.create_restaurant_table()

def createBranchTable():
    return repository.create_branch_table()

def createOrderTable():
    return repository.create_order_table()

def createMenuItemTable():
    return repository.create_menuitem_table()

def createOrderItemTable():
    return repository.create_orderitem_table()

###############################
### Database Fetch Services ###
###############################

# All

def getClientAll():
    return repository.get_table("client")

def getCustomerAll():
    return repository.get_table("customer")

def getRestaurantAll():
    return repository.get_table("restaurant")

def getBranchAll():
    return repository.get_table("branch")

def getOrderAll():
    return repository.get_table("myorder")

def getMenuItemAll():
    return repository.get_table("menuitem")

def getOrderItemAll():
    return repository.get_table("orderitem")

# Column

def getClientCol(col):
    col = str(col)
    if (col not in clientCols):
        return "Column does not exist in Client Table"
    return repository.get_table_col("client", col)

def getCustomerCol(col):
    col = str(col)
    if (col not in customerCols):
        return "Column does not exist in Customer Table"
    return repository.get_table_col("customer", col)

def getRestaurantCol(col):
    col = str(col)
    if (col not in restaurantCols):
        return "Column does not exist in Restaurant Table"
    return repository.get_table_col("restaurant", col)

def getBranchCol(col):
    col = str(col)
    if (col not in branchCols):
        return "Column does not exist in Branch Table"
    return repository.get_table_col("branch", col)

def getOrderCol(col):
    col = str(col)
    if (col not in myorderCols):
        return "Column does not exist in MyOrder Table"
    return repository.get_table_col("myorder", col)

def getMenuItemCol(col):
    col = str(col)
    if (col not in menuitemCols):
        return "Column does not exist in MenuItem Table"
    return repository.get_table_col("menuitem", col)

def getOrderItemCol(col):
    col = str(col)
    if (col not in orderitemCols):
        return "Column does not exist in orderitem Table"
    return repository.get_table_col("orderitem", col)


# Row

def getClientRow(col, val):
    col = str(col)
    if (col not in clientCols):
        return "Column does not exist in Client Table"
    clientsRaw = getClientCol(col)
    clients = []
    for r in clientsRaw:
        clients.append(r[0])
    if (val not in clients):
        return "Value does not exist in Client Table"
    return repository.get_table_row("client", col, val)

def getCustomerRow(col, val):
    col = str(col)
    if (col not in customerCols):
        return "Column does not exist in Customer Table"
    customersRaw = getCustomerCol(col)
    customers = []
    for r in customersRaw:
        customers.append(r[0])
    if (val not in customers):
        return "Value does not exist in Customer Table"
    return repository.get_table_row("customer", col, val)

def getRestaurantRow(col, val):
    col = str(col)
    if (col not in restaurantCols):
        return "Column does not exist in Restaurant Table"
    restaurantsRaw = getRestaurantCol(col)
    restaurants = []
    for r in restaurantsRaw:
        restaurants.append(r[0])
    if (val not in restaurants):
        return "Value does not exist in Restaurant Table"
    return repository.get_table_row("restaurant", col, val)


def getBranchRow(col, val):
    col = str(col)
    if (col not in branchCols):
        return "Column does not exist in Branch Table"
    branchesRaw = getBranchCol(col)
    branches = []
    for r in branchesRaw:
        branches.append(r[0])
    if (val not in branches):
        return "Value does not exist in Branch Table"
    return repository.get_table_row("branch", col, val)

def getOrderRow(col, val):
    col = str(col)
    if (col not in myorderCols):
        return "Column does not exist in MyOrder Table"
    ordersRaw = getOrderCol(col)
    orders = []
    for r in ordersRaw:
        orders.append(r[0])
    if (val not in orders):
        return "Value does not exist in MyOrder Table"
    return repository.get_table_row("myorder", col, val)

def getMenuItemRow(col, val):
    col = str(col)
    if (col not in menuitemCols):
        return "Column does not exist in MenuItem Table"
    menuitemsRaw = getMenuItemCol(col)
    menuitems = []
    for r in menuitemsRaw:
        menuitems.append(r[0])
    if (val not in menuitems):
        return "Value does not exist in MenuItem Table"
    return repository.get_table_row("menuitem", col, val)

def getOrderItemRow(col, val):
    col = str(col)
    if (col not in orderitemCols):
        return "Column does not exist in orderitem Table"
    orderitemsRaw = getOrderItemCol(col)
    orderitems = []
    for r in orderitemsRaw:
        orderitems.append(r[0])
    if (val not in orderitems):
        return "Value does not exist in orderitem Table"
    return repository.get_table_row("orderitem", col, val)



################################
### Database Insert Services ### 
################################

# columns is an array of columns to be inserted into
# values is an array of the corresponding values in each column
def insertClientRow(columns, values):
    for col in columns:
        if (col not in clientCols):
            return "One or more columns does not exist in Client Table"
    if (len(columns) != len(values)):
        return "Columns and values don't match"
    columns = ['client_id'] + columns
    values = [uuid.uuid4().hex] + values
    return repository.insert_row("client", columns, values)

def insertCustomerRow(columns, values):
    for col in columns:
        if (col not in customerCols):
            return "One or more columns does not exist in Customer Table"
    if (len(columns) != len(values)):
        return "Columns and values don't match"
    columns = ['customer_id'] + columns
    values = [uuid.uuid4().hex] + values
    return repository.insert_row("customer", columns, values)

def insertRestaurantRow(columns, values):
    for col in columns:
        if (col not in restaurantCols):
            return "One or more columns does not exist in Restaurant Table"
    if (len(columns) != len(values)):
        return "Columns and values don't match"
    columns = ['restaurant_id'] + columns
    values = [uuid.uuid4().hex] + values
    return repository.insert_row("restaurant", columns, values)

def insertBranchRow(columns, values):
    for col in columns:
        if (col not in branchCols):
            return "One or more columns does not exist in Branch Table"
    if (len(columns) != len(values)):
        return "Columns and values don't match"
    columns = ['branch_id'] + columns
    values = [uuid.uuid4().hex] + values
    return repository.insert_row("branch", columns, values)

def insertOrderRow(columns, values):
    for col in columns:
        if (col not in myorderCols):
            return "One or more columns does not exist in MyOrder Table"
    if (len(columns) != len(values)):
        return "Columns and values don't match"
    columns = ['myorder_id'] + columns
    values = [uuid.uuid4().hex] + values
    return repository.insert_row("myorder", columns, values)

def insertMenuItemRow(columns, values):
    for col in columns:
        if (col not in menuitemCols):
            return "One or more columns does not exist in MenuItem Table"
    if (len(columns) != len(values)):
        return "Columns and values don't match"
    columns = ['menuitem_id'] + columns
    values = [uuid.uuid4().hex] + values
    return repository.insert_row("menuitem", columns, values)

def insertOrderItemRow(columns, values):
    for col in columns:
        if (col not in orderitemCols):
            return "One or more columns does not exist in OrderItem Table"
    if (len(columns) != len(values)):
        return "Columns and values don't match"
    columns = ['orderitem_id'] + columns
    values = [uuid.uuid4().hex] + values
    return repository.insert_row("orderitem", columns, values)



################################
### Database Update Services ### 
################################

# data is a dictionary that stores column : value pairs
# update only at col with row (value in the col) if the arguments are given
def updateClient(data, col=None, row=None):
    for d in data:
        if (d not in clientCols):
            return "One or more columns does not exist in Client Table"
    if (col != None):
        if (col not in clientCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        clientsRaw = getClientCol(col)
        clients = []
        for r in clientsRaw:
            clients.append(r[0])
        if (row not in clients):
            return "Row value does not exist in the Client Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.update_table("client", data, col, row)


def updateCustomer(data, col=None, row=None):
    for d in data:
        if (d not in customerCols):
            return "One or more columns does not exist in Customer Table"
    if (col != None):
        if (col not in customerCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        customersRaw = getCustomerCol(col)
        customers = []
        for r in customersRaw:
            customers.append(r[0])
        if (row not in customers):
            return "Row value does not exist in the Customer Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.update_table("customer", data, col, row)

def updateRestaurant(data, col=None, row=None):
    for d in data:
        if (d not in restaurantCols):
            return "One or more columns does not exist in Restaurant Table"
    if (col != None):
        if (col not in restaurantCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        restaurantsRaw = getRestaurantCol(col)
        restaurants = []
        for r in restaurantsRaw:
            restaurants.append(r[0])
        if (row not in restaurants):
            return "Row value does not exist in the Restaurant Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.update_table("restaurant", data, col, row)


def updateBranch(data, col=None, row=None):
    for d in data:
        if (d not in branchCols):
            return "One or more columns does not exist in Branch Table"
    if (col != None):
        if (col not in branchCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        branchesRaw = getBranchCol(col)
        branches = []
        for r in branchesRaw:
            branches.append(r[0])
        if (row not in branches):
            return "Row value does not exist in the Branch Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.update_table("branch", data, col, row)


def updateOrder(data, col=None, row=None):
    for d in data:
        if (d not in myorderCols):
            return "One or more columns does not exist in MyOrder Table"
    if (col != None):
        if (col not in myorderCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        ordersRaw = getOrderCol(col)
        orders = []
        for r in ordersRaw:
            orders.append(r[0])
        if (row not in orders):
            return "Row value does not exist in the MyOrder Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.update_table("myorder", data, col, row)


def updateMenuItem(data, col=None, row=None):
    for d in data:
        if (d not in menuitemCols):
            return "One or more columns does not exist in MenuItem Table"
    if (col != None):
        if (col not in menuitemCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        menuitemsRaw = getMenuItemCol(col)
        menuitems = []
        for r in menuitemsRaw:
            menuitems.append(r[0])
        if (row not in menuitems):
            return "Row value does not exist in the MenuItem Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.update_table("menuitem", data, col, row)


def updateOrderItem(data, col=None, row=None):
    for d in data:
        if (d not in orderitemCols):
            return "One or more columns does not exist in OrderItem Table"
    if (col != None):
        if (col not in orderitemCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        orderitemsRaw = getOrderItemCol(col)
        orderitems = []
        for r in orderitemsRaw:
            orderitems.append(r[0])
        if (row not in orderitems):
            return "Row value does not exist in the OrderItem Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.update_table("orderitem", data, col, row)



################################
### Database Delete Services ###
################################

# delete only at col with row (value in col) only if arguments are given
# otherwise, delete all rows in the table

def deleteClient(col=None, row=None):
    if (col != None):
        if (col not in clientCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        clientsRaw = getClientCol(col)
        clients = []
        for r in clientsRaw:
            clients.append(r[0])
        if (row not in clients):
            return "Row value does not exist in the Client Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.delete_row("client", col, row)

def deleteCustomer(col=None, row=None):
    if (col != None):
        if (col not in customerCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        customersRaw = getCustomerCol(col)
        customers = []
        for r in customersRaw:
            customers.append(r[0])
        if (row not in customers):
            return "Row value does not exist in the Customer Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.delete_row("customer", col, row)

def deleteRestaurant(col=None, row=None):
    if (col != None):
        if (col not in restaurantCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        restaurantsRaw = getRestaurantCol(col)
        restaurants = []
        for r in restaurantsRaw:
            restaurants.append(r[0])
        if (row not in restaurants):
            return "Row value does not exist in the Restaurant Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.delete_row("restaurant", col, row)

def deleteBranch(col=None, row=None):
    if (col != None):
        if (col not in branchCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        branchesRaw = getBranchCol(col)
        branches = []
        for r in branchesRaw:
            branches.append(r[0])
        if (row not in branches):
            return "Row value does not exist in the Branch Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.delete_row("branch", col, row)

def deleteOrder(col=None, row=None):
    if (col != None):
        if (col not in myorderCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        ordersRaw = getOrderCol(col)
        orders = []
        for r in ordersRaw:
            orders.append(r[0])
        if (row not in orders):
            return "Row value does not exist in the MyOrder Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.delete_row("myorder", col, row)

def deleteMenuItem(col=None, row=None):
    if (col != None):
        if (col not in menuitemCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        menuitemsRaw = getMenuItemCol(col)
        menuitems = []
        for r in menuitemsRaw:
            menuitems.append(r[0])
        if (row not in menuitems):
            return "Row value does not exist in the MenuItem Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.delete_row("menuitem", col, row)

def deleteOrderItem(col=None, row=None):
    if (col != None):
        if (col not in orderitemCols):
            return "Specified col is not a field in the table"
        if (row == None):
            return "Col given but row is not specified"
        orderitemsRaw = getOrderItemCol(col)
        orderitems = []
        for r in orderitemsRaw:
            orderitems.append(r[0])
        if (row not in orderitems):
            return "Row value does not exist in the OrderItem Table"
    else:
        if (row != None):
            return "Row given but col is not specified"
    return repository.delete_row("orderitem", col, row)



##############################
### Miscellaneous Services ###
##############################

def getClientName(session):
    if not session.get('user'):
        email = session['name']
        data = getClientRow("email", email)
        return data[0][1]
    return session['name']


# Registration Authentication Service
class RegistrationForm(Form):
    name = StringField('Name', [validators.InputRequired(), validators.Length(min=1, max=50)], render_kw={"placeholder": "Name", "class": "form-control"})
    email = EmailField('Email', [validators.DataRequired(), validators.Email(message="Invalid email address")], render_kw={"placeholder": "Email", "class": "form-control"})
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=6),
        validators.EqualTo('confirm', message='Passwords must match')
    ], render_kw={"placeholder": "Password", "class": "form-control"})
    confirm = PasswordField('Retype password', [validators.InputRequired()], render_kw={"placeholder": "Retype Password", "class": "form-control"})

    #Check that this email does not already exist in the database
    def validate_email(self, email):
        client = getClientAll()
        for user in client:
            if user[2] == self.email.data:
                raise ValidationError("Email already taken")

