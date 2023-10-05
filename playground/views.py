from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def say_Hello(request):
   return render(request,"myfirst.html",{'name':"Houssin IS the Best "})


