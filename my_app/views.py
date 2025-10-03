from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  return HttpResponse('You are being indexed!')

def about(request):
  return HttpResponse('My name is Andrew Dinh and I am playing with Django!')

def hello(request, first_name):
  return HttpResponse(f"Hello {first_name}")

def add(request, num1, num2):
  return HttpResponse(num1 + num2)