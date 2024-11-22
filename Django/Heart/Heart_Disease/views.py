from imaplib import _Authenticator
from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
import os
from .models import UserRegister
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    #msg="<h1>Welcome to Django Framework</h1>"
   # return HttpResponse(msg)
    #result=os.path.join(BASE_DIR,"templates")
    #print(result)
    return render(request,"home.html")


def result(request):
     mydata=UserRegister.objects.all()

     return render(request,"result.html",{'datas':mydata})


def register(request):
     if request.method=="POST":
          name=request.POST["name"]
          password=request.POST["password"]
          address=request.POST["address"]
          mail=request.POST["mail"]

          obj=UserRegister()
          obj.Name=name
          obj.Password=password
          obj.Address=address
          obj.Mail=mail
          obj.save()
          print(obj.Name)
         # messages.info(request, 'Registration successfull!')
          return render(request,"home.html")
     return render(request,"getpost.html")
     

def login(request):
     if request.method=="POST":
          name=request.POST["name"]
          password=request.POST["password"]
          user = authenticate(request, name = name, password = password)
          if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {name} !!')
            return render(request,"home.html")
          else:
            messages.info(request, f'account done not exit plz sign in')

     return render(request,"login.html")

def userdata(request):
     if request.method=="POST":
          name=request.POST["name"]
          password=request.POST["password"]
          address=request.POST["address"]
          mail=request.POST["mail"]

          obj=UserRegister()
          obj.Name=name
          obj.Password=password
          obj.Address=address
          obj.Mail=mail
          obj.save()
          print(obj.Name)
          messages.info(request, 'Registration successfull!')
          return render(request,"home.html")
     return render(request,"getpost.html")

def index(request):
    #msg="<h1>Welcome to Index Page</h1>"
    return render(request,"index.html")

#def users(request):
    #msg="<h1>Welcome to Index Page</h1>"
 #   return HttpResponse("<h1>Welcome to users Page</h1>")