from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context= {
        'variable':"This is sent"
    }
    if request.method=="POST":
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        phone=request.POST.get('Phone')
        msg=request.POST.get('Msg')
        contact=Contact(name=name,email=email,phone=phone,msg=msg)
        contact.save()
        messages.success(request,'message sent successflly')
       
    return render(request,'index.html',context)
    #return HttpResponse("THIS IS THE HOME PAGE....")

# def about(request):  
#    return render(request,'about.html')
#     #return HttpResponse("THIS IS THE about PAGE....")
 
# def service(request):
#     return render(request,'services.html')
#      #return HttpResponse("THIS IS THE HOME PAGE....")
 
    
# def team(request):
#     return render(request,'team.html')
#     #return HttpResponse("THIS IS THE HOME PAGE....")
 




