from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import pre_save


class Additem(models.Model):
    DrugName = models.CharField(max_length=20)
    Quantity = models.CharField(max_length=20)
    Provider = models.CharField(max_length=30)
    GSTNo = models.CharField(max_length=15)
    Comment = models.TextField(blank=True)
    #Bill = models.ImageField(upload_to='provider/images')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.DrugName

    def has_module_perms(self, app_label):
        return True


class Addstaff(models.Model):
    StaffName = models.CharField(max_length=20)
    Age = models.IntegerField()
    Address = models.TextField(blank=True)
    Qualification = models.CharField(max_length=15)
    StaffId = models.TextField(blank=True)
    IDcard = models.ImageField(upload_to='provider/images')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.StaffId

    def has_module_perms(self, app_label):
        return True
