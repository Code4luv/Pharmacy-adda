# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from .models import Customer
# from django.contrib.auth.models import Group
# #from .views import home


# def customer_profile(sender,instance,created,**kwargs):
#     if created:
#         group = Group.objects.get(name = 'Doctor' )
#         instance.groups.add(group)
#         Customer.objects.create(
#             user = instance,
#             name = instance.username
#         )
#     print("Printing kwargs",kwargs,sender,instance,created)
# post_save.connect(customer_profile, sender=User)