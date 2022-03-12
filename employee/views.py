from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def employee(request):
    return render(request,"employee.html")
    #return HttpResponse("employee page")
