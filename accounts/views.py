from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect


def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in!')
            return redirect('index')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')

    return render(request,'account/login.html')

def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        first_name = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']

    #check if password match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'Sorry,username already taken!')
                return redirect('register')
            else:
            #check mail
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Sorry,email already taken!')
                    return redirect('register')
                else:
                    #register new user
                    user= User.objects.create_user(username=username,email=email,first_name=first_name,last_name=lastname,password=password)
                    user.save()
                    messages.success(request,'You have been registered!')
                    return redirect('login')
        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
    else:
        return render(request,'account/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You have successfully loggedout!')
        return redirect('index')


