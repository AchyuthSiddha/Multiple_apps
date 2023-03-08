from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_First(request):
    return HttpResponse("<h1><mark><marquee>this is App1_First</marquee><h1>")
def app1_Second(request):
    return HttpResponse("<h1><mark><marquee>This is App1_Second</marquee></h1>")