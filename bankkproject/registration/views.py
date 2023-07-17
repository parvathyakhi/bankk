from django.contrib import messages, auth
# from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('message')
        else:
            messages.info(request,'Invalid Registration')
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        conform_password = request.POST['conform-password']
        if password == conform_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
                # print('user created')
        else:
            # print('Password not match')
            messages.info(request,'password not matches')
            return redirect('register')
        # return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def nform(request):
    if request.method == 'POST':
        messages.success(request, 'Application accepted.')


    return render(request,'nform.html')

def message(request):
    return render(request, 'message.html')