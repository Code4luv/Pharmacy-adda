from . import views
from django.urls import path, include
#from Patitent import views

app_name = 'provider'

urlpatterns = [
    path('additem/', views.additem, name='additem'),
    path('displaystock/', views.displaystock, name='displaystock'),
    path('addstaff/', views.addstaff, name = 'addstaff'),
    path('displaystaff/', views.displaystaff, name = 'displaystaff')

]
