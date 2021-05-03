from django.contrib import admin
from .models import Orderdetails


class OrderdeatilsAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Orderdetails,OrderdeatilsAdmin)
