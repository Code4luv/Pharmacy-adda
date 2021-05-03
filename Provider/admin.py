from django.contrib import admin
from .models import Additem,Addstaff


class AddItemAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Additem,AddItemAdmin)

class AddStaffAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Addstaff,AddStaffAdmin)

