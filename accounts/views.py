from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # get form values from POST
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check  if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already Taken try another Username')
                return redirect('register')
            else:
                # Check E-mail
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exist')
                    return redirect('register')
                else:
                    # Create USER
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)

                    # Login after create
                    user.save()
                    messages.success(request, 'You are now registered and can login')
                    return redirect('login')
        else:
            messages.error(request,  'Password do not match')
            return redirect('register')

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