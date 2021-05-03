from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Customer, Patient
from .form import Patientdata,CreateUserForm
from .decorator import unauthenticated_user,allowed_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

def home(request):
    
    
    form = CreateUserForm()
    print(form)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            #username = form.cleaned_data.get('username')
            role = request.POST['role']
            group = Group.objects.get(name=role)
            user.groups.add(group)
            # Customer.objects.create(
            #     user = user,
            #     name = user.name,
            # )
            #messages.success(request, 'Account was created for ' + user)

            return redirect('login')
        

    context = {'form':form}
    return render(request, 'Doctor/home.html', context)

@unauthenticated_user
def login_user(request):
    if request.method=="GET":
        return render(request, 'Doctor/login_page.html')
    if request.method == "POST":
        user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is None:
            return render(request, 'Doctor/login_page.html', {'error1': 'User name and password did not match'})
        else:
            #print(user)
            login(request, user)
            if request.user.groups.filter(name = "Doctor"):
                return redirect('displaypatient')
            if request.user.groups.filter(name = "Provider"):
                return redirect("/Provider/displaystock")
            if request.user.groups.filter(name = "Patitent"):
                return redirect("/Patitent/displayorder")
            else:
                return redirect('home')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required(login_url='login')
@allowed_user(allowed_roles=['Doctor'])
def createpatient(request):
    if request.method == "GET":
        return render(request, 'Doctor/Patient_adddetail.html', {'form': Patientdata()})
    else:
        try:
            form = Patientdata(request.POST, request.FILES)
            newPatient = form.save(commit=False)
            newPatient.user = request.user
            newPatient.save()
            return render(request, 'Doctor/Patient_adddetail.html')
        except ValueError:
            return render(request, 'Doctor/Patient_adddetail.html', {'error2': 'Please enter valid data and ensure to fill all fields'})

@login_required(login_url='login')
@allowed_user(allowed_roles=['Doctor'])
def displaypatient(request):
    display = Patient.objects.filter(user=request.user)

    return render(request, 'Doctor/displaypatient.html', {'display': display})


"""def signupuser(request):
    if request.method == 'GET':
        return render(request,'todo/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request,'todo/signupuser.html',{'form':UserCreationForm(), 'error': 'User name already exist. Please choose other username'})
        else:
            return render(request,'todo/signupuser.html',{'form':UserCreationForm(), 'error': 'Password did not match'})

def currenttodos(request):
    return render(request,'todo/currenttodos.html')"""


"""def loginuser(request):
    if request.method == 'GET':
        return render(request, 'Doctor/home.html')
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'Doctor/home.html', {'error1': 'User name and password did not match'})
        else:
            login(request, user)
            return redirect('home')"""


"""
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
"""
