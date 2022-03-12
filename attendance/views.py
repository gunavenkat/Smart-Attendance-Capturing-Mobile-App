from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def attendance(request):
    return render(request,"attendance.html")
    #return HttpResponse("attendance page")
