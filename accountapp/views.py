from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    if request.method == "POST":
        return render(request, 'accountapp/helloworld.html', context={'text': 'POST method!!'})
    elif request.method == "GET":
        return render(request, 'accountapp/helloworld.html', context={'text': 'GET method!!'})
    
