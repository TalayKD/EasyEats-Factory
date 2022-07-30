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

# OrderItems Table
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

# Education
@app.route('/insertpageEducation')
def insertpageEducation():
    return insertpageEducationController()


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

# Education
@app.route('/updatepageEducation')
def updatepageEducation():
    return updatepageEducationController()


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

# Education
@app.route('/insertdataEducation', methods=['GET', 'POST'])
def insertdataEducation():
    return insertdataEducationController()


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


# Education
@app.route('/updatedataEducation', methods=['GET', 'POST', 'PUT'])
def updatedataEducation():
    return updatedataEducationController()


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

# Education
@app.route('/deleterecordEducation', methods = ['GET','POST','DELETE'])
def deleterecordEducation():
    return deleterecordEducationController()


# Close Database Connection
@app.route('/closedb')
def closedb():
    return closeDB()

if __name__ == "__main__":
    app.run(debug=True)