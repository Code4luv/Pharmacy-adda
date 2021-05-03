from django.forms import ModelForm
from .models import Orderdetails


class OrderDetail(ModelForm):
    class Meta:
        model = Orderdetails
        fields = ['PatitentName','Age','Address','DrugName', 'Quantity', 'Comment', 'Prescription', 'Orderno']
