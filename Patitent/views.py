from django.shortcuts import render
from .form import OrderDetail
from django.contrib.auth.models import User
from .models import Orderdetails
from Doctor.decorator import allowed_user
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
@allowed_user(allowed_roles=['Patitent'])
def orderdetails(request):
    if request.method == "GET":
        return render(request, 'Patitent/orderdetails.html', {'form': OrderDetail()})
    else:
        try:
            form = OrderDetail(request.POST, request.FILES)
            newPatient = form.save(commit=False)
            newPatient.user = request.user
            newPatient.save()
            return render(request, 'Patitent/orderdetails.html')
        except ValueError:
            return render(request, 'Patitent/orderdetails.html', {'error2': 'Please enter valid data and ensure to fill all fields'})


@login_required(login_url='login')
@allowed_user(allowed_roles=['Patitent'])
def displayorder(request):
    order = Orderdetails.objects.filter(user=request.user)

    return render(request, 'Patitent/displayorder.html', {'order': order})
