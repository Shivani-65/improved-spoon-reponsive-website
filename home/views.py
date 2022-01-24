from django.shortcuts import render,HttpResponse
from home.models import Contact , Register
from datetime import datetime
from django.contrib import messages



# Create your views here.
def index(request):
    context={
        "variable1":"i am great",
    }
    return render(request,'index.html',context)
    #return HttpResponse("this is my home page")

def about(request):
        return render(request,'about.html')

#    return HttpResponse("this is my about page")

def team(request):
        return render(request,'team.html')

#    return HttpResponse("this is my team inspiration page")

def gallery(request):
            return render(request,'gallery.html')

#   return HttpResponse("this is my gallery page")

def lifetime(request):
            return render(request,'lifetime.html')

#    return HttpResponse("this is my lifetime membership page")

def distributor(request):
            return render(request,'distributor.html')

    #return HttpResponse("this is my distributor membership page")

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

        



    return render(request,'contact.html')

#    return HttpResponse("this is my lifetime membership page"

def register(request):
        if request.method == 'POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            state=request.POST.get('state')
            city=request.POST.get('city')
            print(name,city)
            register=Register(name=name,email=email,phone=phone,state=state,city=city,date=datetime.today())
            register.save()
            messages.success(request, 'You are registered Successfully!')

        return render(request,'index.html')





