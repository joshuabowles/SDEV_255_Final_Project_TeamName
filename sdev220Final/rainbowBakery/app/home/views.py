from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def Home(request):

    currentTime = datetime.datetime.now()
    currentTime.hour
    if currentTime.hour < 12:
        message = 'Good Morning!'
    elif 12 <= currentTime.hour < 18:
        message = 'Good Afternoon!'
    else:
        message = 'Good Evening!'

    return render(request, "home.html", {"title": "Home Page", "message": message})


def Stock(request):
    return render(request, "stock.html", {"title": "Stock Page", "message": "Hello World"})
