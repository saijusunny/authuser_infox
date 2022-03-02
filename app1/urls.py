from django import views
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('about/', views.about, name='about'),

    path('usercreate/', views.usercreate, name='usercreate'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),

    
]