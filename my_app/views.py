from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  return HttpResponse('You are being indexed!')

def about(request):
  return HttpResponse('My name is Andrew Dinh and I am playing with Django!')