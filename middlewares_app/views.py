from django.shortcuts import render

# Create your views here.

def maintainance_view(request):
    return render(request, 'middlewares_app/maintainance.html')


def home_view(request):
    return render(request,'middlewares_app/home.html')

