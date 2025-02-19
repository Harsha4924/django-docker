from django.http import HttpResponse
from django.shortcuts import render

def my_func(request):
    return render(request, 'myapp/index.html')
