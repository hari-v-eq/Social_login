from django.shortcuts import render, redirect
from . models import User




def login(request):
    
    
    return render(request, 'myapp/home.html')

def signup(request):
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        uid=User.objects.create(email=email,password=password)  
        uid.save()  
        s_msg="Account Created Successfully"
        return render (request, "myapp/login.html",{'s_msg':s_msg})
    else:
        return render (request, "myapp/signup.html")


def home(request):
    return render(request, 'myapp/home.html')

def logout(request):
    if "email" in request.session:
        del request.session['email']
        s_msg="Successfully Logged out"
        return render(request,"myapp/login.html",{'s_msg':s_msg})       
    else:
        return render(request,"myapp/login.html")