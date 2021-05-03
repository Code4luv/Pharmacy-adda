from django.forms import ModelForm
from .models import Patient
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Patientdata(ModelForm):
    class Meta:
        model = Patient
        fields = ['Patient_Name', 'Patient_Id', 'Description', 'Precription']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']