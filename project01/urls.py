"""project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import *
from app2.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1_First/',app1_First,name='app1_First'),
    path('app1_Second/',app1_Second,name='app1_Second'),
    path('app2_Second/',app2_Second,name='app2_Second'),
    path('app2_First/',app2_First,name='app2_First'),
]
