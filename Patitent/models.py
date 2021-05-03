
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
from django.conf import settings
from .utils import unique_orderno_genrator
from django.db.models.signals import pre_save


class Orderdetails(models.Model):
    PatitentName = models.CharField(max_length=20)
    Age = models.IntegerField()
    Address = models.TextField(blank=True)
    
    DrugName = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    Comment = models.TextField(blank=True)
    Prescription = models.ImageField(upload_to='Patitent/images')
    
    Orderno = models.CharField(max_length=10, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    def __str__(self):
        return self.Orderno

    def has_module_perms(self, app_label):
        return True


def pre_save_create_orderno(sender, instance, *args, **kwargs):
    if not instance.Orderno:
        instance.Orderno = unique_orderno_genrator(instance)


pre_save.connect(pre_save_create_orderno, sender=Orderdetails)
