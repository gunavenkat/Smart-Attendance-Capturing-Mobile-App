from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
import sqlite3
from attendance.models import User1
import face_recognition
# Create your views here.
def register(request):
    if request.method =="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        gender=request.POST['gender']
        email=request.POST['email']
        number=request.POST['number']
        employee_id=request.POST['employee_id']
        designation=request.POST['designation']
        office_address=request.POST['office_address']
        password1=request.POST['password']
        if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
                
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            return redirect('register')
                
        else:
            user=User.objects.create_user(username=username, password=password1,email=email,first_name=firstname)
            user.save();
            cursor=sqlite3.connect('staff.sqlite3')
            cursor.execute('INSERT INTO employeedetails VALUES (?,?,?,?,?,?);', (firstname,lastname,gender,employee_id,designation,office_address,))
            cursor.commit()
            cursor.close()
            
            print('user created')
            messages.info(request,'Registered successfully')
            user=auth.authenticate(username=username,password=password1)

            if user is not None:
                auth.login(request,user)
                return redirect('register2')
        
    return render(request,"register.html")
def register2(request):
    if request.method =="POST":
        print("request handling")
        picture=request.FILES['image'];    
        user=User1(pic=picture)
        user.save()
        

        current_user=request.user
        image_status="no job done"
        location_status="Location verified"
        known_image = face_recognition.load_image_file("media/profiles/"+str(current_user.username)+".jpg")
        biden_encoding = face_recognition.face_encodings(known_image)
        
        
        
        if len(biden_encoding)==0:
            
            image_status="NO FACE FOUND, TRY AGAIN !!!"
            current_user=request.user
            empid=str(current_user.username)
            print(empid)
            return render(request,"register2.html",{"Emp_no":empid+".jpg","image_status":image_status})
        else: 
            return redirect("/")

        
    current_user=request.user
    empid=str(current_user.username)
    print(empid)
    return render(request,"register2.html",{"Emp_no":empid+".jpg"})
    
def login(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']


        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid username or password')
            return redirect("login")

    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
