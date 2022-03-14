import sqlite3




cursor=sqlite3.connect('staff.sqlite3')
#firstname
def firstname(employee_id):
    
    l=[]
    first_name=cursor.execute("SELECT first_name from employeedetails WHERE employee_id LIKE (?) ",(employee_id,))
    last_name=cursor.execute("SELECT last_name from employeedetails WHERE employee_id LIKE (?) ",(employee_id,))
    gender=cursor.execute("SELECT  gender from employeedetails WHERE employee_id LIKE (?) ",(employee_id,))
    designation=cursor.execute("SELECT designation from employeedetails WHERE employee_id LIKE (?) ",(employee_id,))
    office=cursor.execute("SELECT office_address from employeedetails WHERE employee_id LIKE (?) ",(employee_id,))
    for i in first_name:
        l.append(i[0])
    for i in last_name :
        l.append(i[0]) 
    for i in gender :
        l.append(i[0]) 
    for i in designation :
        l.append(i[0]) 
    for i in office :
        l.append(i[0])               
    cursor.close()
    return(l)
    

    # query = ("SELECT first_name,last_name,gender,designation,office_address from employeedetails WHERE employee_id LIKE (?) ")
    # cursor.execute(query,employee_id)
    # for (first_name,last_name,gender,designation,office_address) in cursor:
    #     print("{},{},{},{},{}".format(first_name,last_name,gender,designation,office_address))


print(firstname(3421))