from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'variable':"this is sent",
        'send':"this is is ketul"
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is home page")
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'service.html')
def tryy(request):
    return HttpResponse("this page is about try")
def mobile(request):
    return HttpResponse("mobile lelo")
def laptop(request):
    return HttpResponse("laptop lelo")
def something(request):
    return HttpResponse("gaand marao")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,"your data has been saved")
    return render(request,'contact.html')