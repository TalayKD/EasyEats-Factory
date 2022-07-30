from service import *
from flask import session, redirect, render_template, request

def initController():
    createClientTable()
    createCustomerTable()
    createRestaurantTable()
    createBranchTable()
    createOrderTable()
    createMenuItemTable()
    createOrderItemTable()

########################
### Page Controllers ###
########################

### Display Pages ###

def displayController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        restaurant = getRestaurantAll()
        name = getClientName(session)
        return render_template('displayAdmin.html', restaurant=restaurant, name=name)

    except Exception as e:
        print("display student ERROR : " , str(e))
        return "display student ERROR : " + str(e)

def displayBranchController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        branch = getBranchAll()
        restaurant = getRestaurantAll()
        name = getClientName(session)
        return render_template('displayBranch.html', branch=branch, restaurant=restaurant, name=name)

    except Exception as e:
        print("display Branch ERROR : " , str(e))
        return "display Branch ERROR : " + str(e)

def displayMenuItemController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        menuitem = getMenuItemAll()
        restaurant = getRestaurantAll()
        name = getClientName(session)
        return render_template('displayMenuItem.html', menuitem=menuitem, restaurant=restaurant, name=name)

    except Exception as e:
        print("display MenuItem ERROR : " , str(e))
        return "display MenuItem ERROR : " + str(e)

def displayCustomerController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        customer = getCustomerAll()
        name = getClientName(session)
        return render_template('displayCustomer.html', customer=customer, name=name)

    except Exception as e:
        print("display customer ERROR : " , str(e))
        return "display customer ERROR : " + str(e)

def displayOrderController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        customer = getCustomerAll()
        order = getOrderAll()
        branch = getBranchAll()
        name = getClientName(session)
        return render_template('displayOrder.html', customer=customer, order=order, branch=branch, name=name)

    except Exception as e:
        print("display order ERROR : " , str(e))
        return "display order ERROR : " + str(e)

def displayOrderItemController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        orderitem = getOrderItemAll()
        order = getOrderAll()
        menuitem = getMenuItemAll()
        branch = getBranchAll()
        name = getClientName(session)
        return render_template('displayOrderItem.html', orderitem=orderitem, branch=branch, order=order, menuitem=menuitem, name=name)

    except Exception as e:
        print("display order item ERROR : " , str(e))
        return "display order item ERROR : " + str(e)


### Insert Form Pages ###

def insertpageController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        name = getClientName(session)
        return render_template('formAdmin.html', name=name)

    except Exception as e:
        print("restaurant form ERROR : " , str(e)) 
        return "restaurant form ERROR : " + str(e)

def insertpageBranchController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        
        restaurant = getRestaurantAll()
        name = getClientName(session)
        return render_template('formBranch.html', restaurant=restaurant, name=name)

    except Exception as e:
        print("restaurant form ERROR : " , str(e)) 
        return "restaurant form ERROR : " + str(e)

def insertpageMenuItemController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        restaurant = getRestaurantAll()
        name = getClientName(session)
        return render_template('formMenuItem.html', restaurant=restaurant, name=name)

    except Exception as e:
        print("menuitem form ERROR : " , str(e)) 
        return "menuitem form ERROR : " + str(e)

def insertpageEducationController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        data = []
        data.append(getClientName(session))
        return render_template('formEd.html', data=data)

    except Exception as e:
        print("education form ERROR : " , str(e))
        return "education form ERROR : " + str(e)

### Update Form Pages ###

def updatepageController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')    

        # Connect to database
        rest = getRestaurantRow("restaurant_id", request.args.get("restaurant_id"))[0]
        name = getClientName(session)
        # student = getStudentRow("student_id", request.args.get("student_id"))
        # data.append(student[0])
        # data.append(getClientName(session))
        return render_template('updateformAdmin.html', rest=rest, name=name)

    except Exception as e:
        print("restaurant update page ERROR : " , str(e)) 
        return "restaurant update page ERROR : " + str(e)

def updatepageBranchController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')    

        # Connect to database
        restaurant = getRestaurantAll()
        bran = getBranchRow("branch_id", request.args.get("branch_id"))[0]
        name = getClientName(session)
        return render_template('updateformBranch.html', restaurant=restaurant, bran=bran, name=name)

    except Exception as e:
        print("branch update page ERROR : " , str(e)) 
        return "branch update page ERROR : " + str(e)

def updatepageMenuItemController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')    

        # Connect to database
        restaurant = getRestaurantAll()
        item = getMenuItemRow("menuitem_id", request.args.get("menuitem_id"))[0]
        print(item)
        name = getClientName(session)
        return render_template('updateformMenuItem.html', restaurant=restaurant, item=item, name=name)

    except Exception as e:
        print("menuitem update page ERROR : " , str(e)) 
        return "menuitem update page ERROR : " + str(e)


def updatepageEducationController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        education = getEducationRow("education_id", request.args.get("education_id"))
        data = []
        data.append(education[0])
        data.append(getClientName(session))
        return render_template('updateformEd.html', data=data)

    except Exception as e:
        print("education update page ERROR : " , str(e)) 
        return "education update page ERROR : " + str(e)

##########################
### Action Controllers ###
##########################

### Insert Data ###

def insertdataController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        data = request.form
        insertRestaurantRow(list(data.keys()), list(data.values()))
        return redirect("/")

    except Exception as e:
        print("insert restaurant ERROR : " , str(e))
        return "insert restaurant ERROR : " + str(e)

def insertdataBranchController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        data = request.form
        insertBranchRow(list(data.keys()), list(data.values()))
        return redirect("/displayBranch")

    except Exception as e:
        print("insert branch ERROR : " , str(e))
        return "insert branch ERROR : " + str(e)

def insertdataMenuItemController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        data = request.form
        print(data)
        insertMenuItemRow(list(data.keys()), list(data.values()))
        return redirect("/displayMenuItem")

    except Exception as e:
        print("insert menuitem ERROR : " , str(e))
        return "insert menuitem ERROR : " + str(e)

def insertdataEducationController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        data = request.form
        insertEducationRow(list(data.keys()), list(data.values()))
        return redirect("/displayEducation")

    except Exception as e:
        print("insert education ERROR : " , str(e))
        return "insert education ERROR : " + str(e)

### Update Data ###

def updatedataController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        data = request.form
        print(data)
        arguments = request.args
        if ('restaurant_id' in arguments):
            updateRestaurant(data, "restaurant_id", arguments.get('restaurant_id'))
        else:
            updateRestaurant(data)
        return redirect("/")

    except Exception as e:
        print("update restaurant ERROR : " , str(e))
        return "update restaurant ERROR : " + str(e)


def updatedataBranchController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        data = request.form
        print(data)
        arguments = request.args
        if ('branch_id' in arguments):
            updateBranch(data, "branch_id", arguments.get('branch_id'))
        else:
            updateBranch(data)
        return redirect("/displayBranch")

    except Exception as e:
        print("update branch ERROR : " , str(e))
        return "update branch ERROR : " + str(e)

def updatedataMenuItemController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        data = request.form
        print(data)
        arguments = request.args
        if ('menuitem_id' in arguments):
            updateMenuItem(data, "menuitem_id", arguments.get('menuitem_id'))
        else:
            updateMenuItem(data)
        return redirect("/displayMenuItem")

    except Exception as e:
        print("update menuitem ERROR : " , str(e))
        return "update menuitem ERROR : " + str(e)


def updatedataEducationController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        data = request.form
        arguments = request.args
        if ('education_id' in arguments):
            updateEducation(data, "education_id", arguments.get('education_id'))
        else:
            updateEducation(data)
        return redirect("/displayEducation")

    except Exception as e:
        print("update education ERROR : " , str(e))
        return "update education ERROR : " + str(e)
    
    
### Delete Data ###

def deleterecordController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        argument = request.args
        if ('restaurant_id' not in argument):
            deleteRestaurant()
        else:
            deleteRestaurant("restaurant_id", argument.get('restaurant_id'))
        return redirect("/")

    except Exception as e:
        print("delete restaurant ERROR : " , str(e))
        return "delete restaurant ERROR : " + str(e)

def deleterecordBranchController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        argument = request.args
        if ('branch_id' not in argument):
            deleteBranch()
        else:
            deleteBranch("branch_id", argument.get('branch_id'))
        return redirect("/displayBranch")

    except Exception as e:
        print("delete branch ERROR : " , str(e))
        return "delete branch ERROR : " + str(e)

def deleterecordMenuItemController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        argument = request.args
        if ('menuitem_id' not in argument):
            deleteMenuItem()
        else:
            deleteMenuItem("menuitem_id", argument.get('menuitem_id'))
        return redirect("/displayMenuItem")

    except Exception as e:
        print("delete menuitem ERROR : " , str(e))
        return "delete menuitem ERROR : " + str(e)

def deleterecordEducationController():
    try:
        # Logs user out if not logged in
        if not session.get('name'):
            return redirect('/loginpage')

        #for use with postman
        #data = request.get_json(force=True)
        argument = request.args
        if ('education_id' not in argument):
            deleteEducation()
        else:
            deleteEducation("education_id", argument.get('education_id'))
        return redirect("/displayEducation")

    except Exception as e:
        data = []
        data.append(str(e))
        data.append(getClientName(session))
        return render_template("errorpage.html", data=data)
