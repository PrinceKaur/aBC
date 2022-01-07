"""apitask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.authtoken import views
from django.contrib import admin
# from knox import views as knox_views
from task import views
from django.urls import path,include
from task.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/register/',SnippetList.as_view(), name='register'),
    path('task/register1/',SnippetList1.as_view(), name='register'),
    path('task/login/', views.login, name='login'),
    path('task/Product/',productlist.as_view(), name='product'),
   
 
]



