import email
from django.http import HttpResponse
from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact

from django.contrib import messages

# Create your views here.
def index(request):
    messages.success(request,"this is a test message")
    
    return render(request,'index.html')

    #return HttpResponse("this is homepage")
def about(request):
    return render(request,'about.html')
 #return HttpResponse("this is aboutpage")

def services(request):
    return render(request,'services.html')
 #return HttpResponse("this is servicespage")
   
def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact=Contact(email=email,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your request has been sent!') 
        
     
    return render(request,'contact.html')
 #return HttpResponse("this is contactpage")