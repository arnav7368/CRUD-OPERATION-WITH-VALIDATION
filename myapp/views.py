from django.shortcuts import render,HttpResponseRedirect
from .models import Employee

# Create your views here.
def Home(request):
    data=Employee.objects.all()
    return render(request,"home.html",{"data":data})

def Add(request):
    if(request.method=="POST"):
        e=Employee()
        e.name=request.POST.get("name")
        e.email=request.POST.get("email")
        e.phone=request.POST.get("phone")
        e.city=request.POST.get("city")
        e.state=request.POST.get("state")
        e.save()
        return HttpResponseRedirect("/")
    return render(request,"add.html")

def Edit(request,id):
    try:
        data=Employee.objects.get(id=id)
        if(request.method=="POST"):
            data.name=request.POST.get("name")
            data.email=request.POST.get("email")
            data.phone=request.POST.get("phone")
            data.city=request.POST.get("city")
            data.state=request.POST.get("state")
            data.save()
            return HttpResponseRedirect("/")
        return render(request,"update.html",{"data":data})
    except:
        pass
    return HttpResponseRedirect("/")

def delete(request,id):
    try:
        data=Employee.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect("/")
    except:
        pass
    return HttpResponseRedirect("/")
    