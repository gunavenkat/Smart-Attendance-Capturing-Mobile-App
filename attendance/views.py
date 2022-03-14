from django.shortcuts import render
from .models import User
# Create your views here.

from django.http import HttpResponse

def attendance(request):
    users=User.objects.all();
    p=users[len(users)-1].pic
    print(p.url)
    return render(request,"attendance.html")
    #return HttpResponse("attendance page")
def uploadimage(request):
    print("request handling")
    picture=request.FILES['image'];
    
    
    user=User(pic=picture)
    user.save();
    
    return render(request,"uploaded.html")

