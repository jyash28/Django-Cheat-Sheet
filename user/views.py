from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login as authorize,logout as deauth

# Create your views here.
def login(request):
    if (request.method == 'POST'):
        form=AuthenticationForm()
        uname=request.POST['username']
        upass=request.POST['password']
        user=authenticate(username=uname,password=upass)
        if user is  None:
            messages.info(request,'Username and Password is not Correct')
            return redirect('/user/login')
        else:
            authorize(request,user)
            return redirect('/user/profile')
    else:
        if (request.user.is_authenticated):
            return redirect('/user/profile')
        form=AuthenticationForm()
    return render(request,'login.html',{'title':'User Login','form':form})


def register(request):
    form=UserCreationForm()
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'User Successfully Registered')
            return redirect('/user/login')
    return render(request,'register.html',{'title':'User Register','form':form})

def logout(request):
    if request.user.is_authenticated:
        deauth(request)
        messages.info(request,"You Have Successfully Loggd Out")
    return redirect('/user/login')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        messages.info(request,"You Need To Login First ")
        return redirect('/user/login')