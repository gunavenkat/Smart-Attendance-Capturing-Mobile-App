from django.shortcuts import render
import sqlite3
# Create your views here.
from django.http import HttpResponse
def firstname(employee_id):
    l=[]
    cursor=sqlite3.connect('staff.sqlite3')
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
    
def employee(request):
    employee_id=3421
    l=firstname(employee_id)
    return render(request,"employee.html",{"First_name":l[0],"Last_name":l[1],"Emp_no":employee_id,"gender":l[2],"designation":l[3],"office_address":l[4]})

