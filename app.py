from __init__ import *
from appController import *
from authentication import *
# temporary
from service import *

### DISPLAY PAGE ###

# Restaurants Table
@app.route('/')
def display():
    return displayController()

# Branches Table
@app.route('/displayBranch')
def displayBranch():
    return displayBranchController()

# Menu Item Table
@app.route('/displayMenuItem')
def displayMenuItem():
    return displayMenuItemController()

# Customer Table
@app.route('/displayCustomer')
def displayCustomer():
    return displayCustomerController()

# Order Table
@app.route('/displayOrder')
def displayOrder():
    return displayOrderController()

# OrderItem Table
@app.route('/displayOrderItem')
def displayOrderItem():
    return displayOrderItemController()


### INSERT FORM PAGE ###

# Restaurant
@app.route('/insertpage')
def insertpage():
    return insertpageController()

# Branch
@app.route('/insertpageBranch')
def insertpageBranch():
    return insertpageBranchController()

# MenuItem
@app.route('/insertpageMenuItem')
def insertpageMenuItem():
    return insertpageMenuItemController()

# Customer
@app.route('/insertpageCustomer')
def insertpageCustomer():
    return insertpageCustomerController()

# Order
@app.route('/insertpageOrder')
def insertpageOrder():
    return insertpageOrderController()

# OrderItem
@app.route('/insertpageOrderItem')
def insertpageOrderItem():
    return insertpageOrderItemController()



### UPDATE FORM PAGE ###

# Restaurant
@app.route('/updatepage')
def updatepage():
    return updatepageController()

# Branch
@app.route('/updatepageBranch')
def updatepageBranch():
    return updatepageBranchController()

# MenuItem
@app.route('/updatepageMenuItem')
def updatepageMenuItem():
    return updatepageMenuItemController()

# Customer
@app.route('/updatepageCustomer')
def updatepageCustomer():
    return updatepageCustomerController()

# Order
@app.route('/updatepageOrder')
def updatepageOrder():
    return updatepageOrderController()

# OrderItem
@app.route('/updatepageOrderItem')
def updatepageOrderItem():
    return updatepageOrderItemController()




# ACTIONS #

### INSERT DATA ###

# Restaurant
@app.route('/insertdata', methods=['GET', 'POST'])
def insertdata():
    return insertdataController()

# Branch
@app.route('/insertdataBranch', methods=['GET', 'POST'])
def insertdataBranch():
    return insertdataBranchController()

# MenuItem
@app.route('/insertdataMenuItem', methods=['GET', 'POST'])
def insertdataMenuItem():
    return insertdataMenuItemController()

# Customer
@app.route('/insertdataCustomer', methods=['GET', 'POST'])
def insertdataCustomer():
    return insertdataCustomerController()

# Order
@app.route('/insertdataOrder', methods=['GET', 'POST'])
def insertdataOrder():
    return insertdataOrderController()

# OrderItem
@app.route('/insertdataOrderItem', methods=['GET', 'POST'])
def insertdataOrderItem():
    return insertdataOrderItemController()



### UPDATE DATA ###

# Restaurant
@app.route('/updatedata', methods=['GET', 'POST', 'PUT'])
def updatedata():
    return updatedataController()


# Branch
@app.route('/updatedataBranch', methods=['GET', 'POST', 'PUT'])
def updatedataBranch():
    return updatedataBranchController()

# MenuItem
@app.route('/updatedataMenuItem', methods=['GET', 'POST', 'PUT'])
def updatedataMenuItem():
    return updatedataMenuItemController()

# Customer
@app.route('/updatedataCustomer', methods=['GET', 'POST', 'PUT'])
def updatedataCustomer():
    return updatedataCustomerController()

# Order
@app.route('/updatedataOrder', methods=['GET', 'POST', 'PUT'])
def updatedataOrder():
    return updatedataOrderController()

# OrderItem
@app.route('/updatedataOrderItem', methods=['GET', 'POST', 'PUT'])
def updatedataOrderItem():
    return updatedataOrderItemController()



### DELETE RECORD ###

# Restaurant
@app.route('/deleterecord', methods = ['GET','POST','DELETE'])
def deleterecord():
    return deleterecordController()

# Branch
@app.route('/deleterecordBranch', methods = ['GET','POST','DELETE'])
def deleterecordBranch():
    return deleterecordBranchController()

# MenuItem
@app.route('/deleterecordMenuItem', methods = ['GET','POST','DELETE'])
def deleterecordMenuItem():
    return deleterecordMenuItemController()

# Customer
@app.route('/deleterecordCustomer', methods = ['GET','POST','DELETE'])
def deleterecordCustomer():
    return deleterecordCustomerController()

# Order
@app.route('/deleterecordOrder', methods = ['GET','POST','DELETE'])
def deleterecordOrder():
    return deleterecordOrderController()

# OrderItem
@app.route('/deleterecordOrderItem', methods = ['GET','POST','DELETE'])
def deleterecordOrderItem():
    return deleterecordOrderItemController()



# Close Database Connection
@app.route('/closedb')
def closedb():
    return closeDB()

if __name__ == "__main__":
    app.run(debug=True)