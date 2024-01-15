from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from requests import request

# Create your views here.
def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=auth.authenticate(username=email,password=password)

        if user is not None:
            auth.login(request, user)
            print("User logged in successfully")
            return redirect('credentials:order')
        else:
            messages.info(request, "Invalid credentials.")
            return redirect("credentials:login")
    return render(request, "login.html")
    

def register(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('credentials:register')
            else:    
                user=User.objects.create_user(username=email,password=password,email=email)
                user.save()
                print("User created successfully")
                return redirect('credentials:login')
        else:
            print("Password not matching")
            return redirect('credentials:register')
    return render(request, 'register.html')


def order(request):
    return render(request, 'order.html')

def logout(request):
    auth.logout(request)
    return redirect('credentials:login')