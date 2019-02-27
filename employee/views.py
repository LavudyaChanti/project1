from django.shortcuts import render
from employee.models import Emp
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def reg(request):
    return render(request,'reg.html')

def regprocess(request):
    #Read Form parameters
    v1=request.GET.get('n1')
    v2 = request.GET.get('n2')
    v3 = request.GET.get('n3')
    v4 = request.GET.get('n4')
    v5 = request.GET.get('n5')

    ob1=Emp(userid=v1,password=v2,fullname=v3,mailid=v4,address=v5)
    ob1.save()
    return render(request,'regsuccess.html',{'msg':'Registration Done Successfully'})

def regsuccess(request):
    return render(request,'regsuccess.html')

def regerror(request):
    return render(request,'regerror.html')

def delete(request):
    return render(request,'delete.html')

def show(request):
    res=Emp.objects.all()
    data='<table border=1><tr><th>Userid</th><th>Password</th><th>Fullname</th><th>mailid</th><th>Address</th></tr>'
    for i in res:
        data=data+'<tr>'
        data=data+'<td>'+i.userid+"</td>"
        data = data + '<td>' + i.password + "</td>"
        data = data + '<td>' + i.fullname + "</td>"
        data = data + '<td>' + i.mailid + "</td>"
        data = data + '<td>' + i.address + "</td>"
        data = data + '</tr>'
    data = data + '</table>'
    data = data + '''<br><br>   <a href={% url 'home' %}>Home</a>'''
    return HttpResponse(data)

def deleteprocess(request):
    v1 = request.GET.get('n1')
    data=Emp.objects.get(userid=v1)
    data.delete()
    return render(request, 'deletesuccess.html',{"msg":"deleted successfully"})