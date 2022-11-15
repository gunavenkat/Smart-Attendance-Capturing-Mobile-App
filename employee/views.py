from django.shortcuts import render
import sqlite3
# Create your views here.
from django.http import HttpResponse
def empDetails(first_name):
    cursor=sqlite3.connect('staff.sqlite3')
    k=cursor.execute("SELECT * from employeedetails WHERE first_name LIKE (?) ",(first_name,))  
    details=k.fetchone()
    print(details)
    cursor.close()
    return(details)
    
def employee(request):
    current_user=request.user
    first_name=current_user.first_name
    print(current_user.first_name)
    l=empDetails(first_name)
    if len(l)==0:
        l=["","","","","",""]
    return render(request,"employee.html",{"First_name":l[0],"Last_name":l[1],"gender":l[2],"Emp_no":l[3],"designation":l[4],"office_address":l[5]})