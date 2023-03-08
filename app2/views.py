from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_Second(request):
    return HttpResponse('<h1><mark><marquee> this is App2_second</marquee></h1>')
def app2_First(request):
    return HttpResponse('<h1><mark><marquee>This is App2_First</marquee></h1>')