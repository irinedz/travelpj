from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username =request.POST['username']
        password =request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")



def register(request):


    if request.method=='POST':
        uname = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        passworda = request.POST['password']
        passwordb = request.POST['passwordx']
        if passworda==passwordb:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username Taken")
                return  redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return  redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=passworda,first_name=fname,last_name=lname,email=email)

                user.save();
                return redirect('login')

        else:

            messages.info(request, "password incorrect")
            return redirect('register')

        return redirect('/')


    return  render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')