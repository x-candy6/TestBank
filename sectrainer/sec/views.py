from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("sec home")

def login(request):
    return HttpResponse("sec home")

def register(request):
    return HttpResponse("sec home")

def logout(request):
    return HttpResponse("sec home")

def error(request):
    return HttpResponse("sec home")

def CreateTest(request):
    return HttpResponse("Create Test")

def TestPage(request):
    return HttpResponse("Create Test")

def Results(request):
    return HttpResponse("Create Test")

def Statistics(request):
    return HttpResponse("Create Test")

def PreviousTests(request):
    return HttpResponse("Create Test")
# Create your views here.
