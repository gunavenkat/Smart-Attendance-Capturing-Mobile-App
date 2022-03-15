from django.shortcuts import render
from .models import User
import face_recognition
# Create your views here.

from django.http import HttpResponse

def attendance(request):
    current_user=request.user
    empid=str(current_user.username)
    print(empid)

    users=User.objects.all();
    p=users[len(users)-1].pic
    print(p.url)
    return render(request,"attendance.html",{"Emp_no":empid+".jpg"})
    #return HttpResponse("attendance page")
def uploadimage(request):
    print("request handling")
    picture=request.FILES['image'];    
    user=User(pic=picture)
    user.save();
    users=User.objects.all();
    p=users[len(users)-1].pic
    print(p.url)

    current_user=request.user
    image_status="no job done"
    location_status="Location verified"
    known_image = face_recognition.load_image_file("media/profiles/"+str(current_user.username)+".jpg")
    unknown_image = face_recognition.load_image_file(str(p.url)[1:])

    biden_encoding = face_recognition.face_encodings(known_image)
    unknown_encoding = face_recognition.face_encodings(unknown_image)
    
    
    
    if len(biden_encoding)==0 or len(unknown_encoding)==0:
        
        image_status="NO FACE FOUND, TRY AGAIN"
    else:
        biden_encoding = biden_encoding[0]
        unknown_encoding = unknown_encoding[0]
        results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
        print(results)
        if (results[0]):
            image_status="Image verified"
            print("matched")
        else:
            image_status="Image not verified,Try again"
            print("no match")
    
    
    return render(request,"uploaded.html",{"image_status":image_status,"location_status":location_status})

