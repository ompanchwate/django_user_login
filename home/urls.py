from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    # Load index function when the url is empty
    path('', views.index, name="home"), 
    
    # Load login function when the url has login
    path('login', views.loginUser, name="login"),
    
    # Load logout when the url has logout
    path('logout', views.logoutUser, name="logoutuser"),
]

