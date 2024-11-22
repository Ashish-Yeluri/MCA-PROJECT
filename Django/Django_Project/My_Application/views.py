from django.shortcuts import render
from django.http import HttpResponse
from .models import UserRegister
#create your views here
def home(request):

   return render(request,"home.html")
def calc(request):
       val1=int (request.GET["a"])
       val2=int (request.GET["b"])
       val3=int (request.GET["c"])
      
       return render(request,"result.html",{'Total':Total})

def register(request):
    name=request.GET["name"]
    password=request.GET["password"]
    email=request.GET["email"]
    address=request.GET["address"]

    obj=UserRegister()
    obj.Nmae=name
    obj.Password=password
    obj.Email=email
    obj.Address=address
    obj.save()
    
    return render(request,"home.html")



    

