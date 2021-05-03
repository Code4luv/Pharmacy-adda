from django.shortcuts import render
from .form import AddItem, AddStaff
from django.contrib.auth.models import User
from .models import Additem, Addstaff
from django.contrib.auth.decorators import login_required
from Doctor.decorator import allowed_user


@login_required(login_url='login')
@allowed_user(allowed_roles=['Provider'])
def additem(request):
    data = {}
    if request.method == "GET":
        return render(request, 'provider/additem.html', {'form': AddItem()})
    else:
        try:
            csv_file = request.FILES['csv_file']
            if not csv_file.name.endswith('.csv'):
                return render(request, "provider/additem.html", {'error2': 'Please upload csv file'})
            file_data = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            for line in lines:
                fields = line.split(",")
                if len(fields) == 5:
                    data_dict = {}
                    data_dict["DrugName"] = fields[0]
                    data_dict["Quantity"] = fields[1]
                    data_dict["Provider"] = fields[2]
                    data_dict["GSTNo"] = fields[3]
                    data_dict["Comment"] = fields[4]
                    # try:
                    form = AddItem(data_dict)
                    if form.is_valid():
                        newPatient = form.save(commit=False)
                        newPatient.user = request.user
                        newPatient.save()
            return render(request, 'provider/additem.html')
        except ValueError:
            return render(request, 'provider/additem.html', {'error2': 'Please enter valid data and ensure to fill all fields'})


@login_required(login_url='login')
@allowed_user(allowed_roles=['Provider'])
def displaystock(request):
    item = Additem.objects.filter(user=request.user)

    return render(request, 'provider/displaystock.html', {'item': item})


@login_required(login_url='login')
@allowed_user(allowed_roles=['Provider'])
def addstaff(request):
    if request.method == "GET":
        return render(request, 'provider/addstaff.html', {'form': AddStaff()})
    else:
        # try:
        form = AddStaff(request.POST, request.FILES)
        newPatient = form.save(commit=False)
        newPatient.user = request.user
        newPatient.save()
        return render(request, 'provider/addstaff.html')
        # except ValueError:
        #    return render(request, 'provider/addstaff.html', {'error2': 'Please enter valid data and ensure to fill all fields'})


@login_required(login_url='login')
@allowed_user(allowed_roles=['Provider'])
def displaystaff(request):
    staff = Addstaff.objects.filter(user=request.user)

    return render(request, 'provider/displaystaff.html', {'staff': staff})
