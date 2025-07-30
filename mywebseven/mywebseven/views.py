from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hello, this is the home page of my web application!")