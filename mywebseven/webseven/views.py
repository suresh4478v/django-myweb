from django.shortcuts import render

# Create your views here.
def all_seven(request):
    return render(request, 'webseven/all_seven.html')
