from django.shortcuts import render,redirect
from .models import Contact
from django.http import HttpResponse


# Create your views here.

def index(request):
    if request.method=="POST":
        Contact=Contact()
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        Contact.name=name
        Contact.phone=phone
        Contact.email=email
        Contact.subject=subject
        Contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACT US</h1>")
    return render(request,'index.html')
