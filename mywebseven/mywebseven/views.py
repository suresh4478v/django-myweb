from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("Hello, this is the home page of my web application!")
    return render(request, 'index.html')

def About(request):
    # return HttpResponse("Hello, this is the about page of my web application!")
    return render(request, 'about.html')

def Contact(request):
    # return HttpResponse("Hello, this is the contact page of my web application!")
    return render(request, 'contacts.html')