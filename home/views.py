from pydoc import render_doc
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import logout, authenticate, login
# Create your views here.

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    
    return render(request,'index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(username, password)
        
        user = authenticate(request,username=username , password= password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            return render(request,'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

