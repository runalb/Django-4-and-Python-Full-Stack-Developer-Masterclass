from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def simple_view(request):
    return HttpResponse("Simple View")

def string_view(request,value):
    return HttpResponse(f"String: {value}")

def int_view(request,value):
    return HttpResponse(f"intiger: {value}")

def slug_view(request,value):
    return HttpResponse(f"slug: {value}")
