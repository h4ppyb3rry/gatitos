from django.urls import path, include
from .import views

app_name = 'users'
urlpatterns = [
    #home page
    path('',include('django.contrib.auth.urls')),
    path('logout/', views.logoutt, name='logout'),
    path('register/', views.register, name='register'),
]