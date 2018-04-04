from django.shortcuts import render
from .models import employee

# Create your views here.


def register(request):
    return render(request, "employee/register.html")


def registration(request):
    e = employee(employee_id = request.POST['employee_id'],employee_name = request.POST['employee_name'],employee_department = request.POST['employee_department'],employee_sal = request.POST['employee_sal'],employee_dob=request.POST['employee_dob'],employee_designation = request.POST['employee_designation'])
    e.save()
    return render(request,"employee/register.html")

def display(request,eid):
    emp = employee.objects.get(employee_id=eid)
    return render(request,"employee/display.html",{'employee':emp})

def starts(request):
    employees = employee.objects.filter(employee_name__startswith = 'A')
    return render(request,"employee/starts.html",{'employees':employees})
