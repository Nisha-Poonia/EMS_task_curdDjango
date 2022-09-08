from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from ems.models import Employee
from django.http import HttpResponse


def ems_view(request):
    if request.method=='GET':
        resp=render(request,'ems/ems.html')
        return resp
    elif request.method=='POST':
        if 'btnadd' in request.POST:
            emp=Employee()
            emp.name=request.POST.get('textname','NA')
            emp.address=request.POST.get('textaddress','NA')
            emp.age=int(request.POST.get('textage',0))
            emp.city=request.POST.get('textcity','NA')
            emp.salary=int(request.POST.get('textsalary',0))
            emp.designation=request.POST.get('textdesig','NA')
            emp.save()
            resp=HttpResponse("<h1> Employee Added SuccessFully!! whose ID : "+str(emp.id)+"</h1>")
            return resp
        elif 'btnsearch' in request.POST:
            empid=int(request.POST.get('textempid',0))
            emp=Employee.objects.get(id=empid)
            d1={'emp':emp}
            resp=render(request,'ems/ems.html',context=d1)
            return resp 
        elif 'btnupdate' in request.POST:
            emp=Employee()
            emp.id=int(request.POST.get('textempid',0))
            if Employee.objects.filter(id=emp.id).exists():
                emp.name=request.POST.get('textname','NA')
                emp.address=request.POST.get('textaddress','NA')
                emp.age=int(request.POST.get('textage','0'))
                emp.city=request.POST.get('textcity','NA')
                emp.salary=int(request.POST.get('textsalary',0))
                emp.designation=request.POST.get('textdesig','NA')
                emp.save()
                resp=HttpResponse("<h1> Employee Update SuccessFully!! whose ID : "+str(emp.id)+"</h1>")
                return resp

        elif 'btndelete' in request.POST:
            emp=Employee()
            emp.id=int(request.POST.get('textempid',0))
            Employee.objects.filter(id=emp.id).delete()
            resp=HttpResponse("<h1>Employee Deleted SuccessFully!! whose ID : "+str(emp.id)+"</h1>")
            return resp

        elif 'btnshow' in request.POST:
            allemp=Employee.objects.all()
            d1={'allemp':allemp}
            resp=render(request,'ems/ems.html',context=d1)
            return resp


