from django.shortcuts import render
from WebApp.models import Emp

def Emp_View(request):
    EmpList = Emp.objects.all()
    My_Dict = {'elist': EmpList}
    return render(request, 'WebApp/Welcome.html', My_Dict)