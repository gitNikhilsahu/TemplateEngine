from django.contrib import admin
from WebApp.models import Emp

class EmpAdmin(admin.ModelAdmin):
    list_display = ['EmpID', 'EmpName', 'EmpSal', 'EmpAdd']

admin.site.register(Emp, EmpAdmin)