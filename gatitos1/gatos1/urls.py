from django.urls import path, include
from .import views

app_name = 'gatos1'
urlpatterns = [
    #home page
    path('', views.principal, name='principal'),
    
    #reservaciones 
    path('reservaciones/', views.reservaciones, name='reservaciones'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('misreservaciones/', views.misreservaciones, name='misreservaciones'),
]