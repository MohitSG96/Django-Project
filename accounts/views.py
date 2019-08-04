from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        # TODO CREATE REGISTRATION LOGIC
        messages.error(request,'Testing error messages')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

    return render(request,'accounts/register.html')
    
def login(request):
    if request.method == 'POST':
        # TODO CREATE LOGIN LOGIC
        pass
    else:
        return render(request, 'accounts/login.html')
    return render(request,'accounts/login.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def logout(request):
    return redirect('index')