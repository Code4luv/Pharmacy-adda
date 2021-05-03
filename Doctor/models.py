from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
from django.conf import settings






class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

   

class Patient(models.Model):
    Patient_Name = models.CharField(max_length=100)
    Patient_Id = models.CharField(max_length=10)
    Description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    Precription = models.ImageField(upload_to='Doctor/images/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.Patient_Name

    def has_module_perms(self, app_label):
        return True


