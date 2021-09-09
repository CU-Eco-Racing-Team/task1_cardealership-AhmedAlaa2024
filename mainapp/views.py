from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, id):
    return HttpResponse("Hello, World! Your ID is {}".format(id))