from django.forms import ModelForm
from .models import Additem, Addstaff


class AddItem(ModelForm):
    class Meta:
        model = Additem
        fields = ['DrugName', 'Quantity', 'Provider', 'GSTNo', 'Comment']


class AddStaff(ModelForm):
    class Meta:
        model = Addstaff
        fields = ['StaffName', 'Age', 'Address',
                  'Qualification', 'StaffId', 'IDcard']
