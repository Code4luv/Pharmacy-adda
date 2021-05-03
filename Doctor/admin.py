from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Patient





class PatientAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Patient, PatientAdmin)
