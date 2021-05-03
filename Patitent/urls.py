from . import views
from django.urls import path, include
#from Patitent import views

app_name = 'Patitent'

urlpatterns = [
    path('orderdetails/', views.orderdetails, name='orderdetails'),
    path('displayorder/', views.displayorder, name='displayorder')

]
