from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.

def hello(request):
    #return HttpResponse("hello world")
    return render_to_response("index.html")

def hw(request):
    #return HttpResponse("hello world")
    return render_to_response("index.html")
