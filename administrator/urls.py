"""employment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from administrator import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('administrator/', views.administrator, name='administrator'),

    path('administrator_register/',views.administrator_register.as_view(), name='administrator_register'),
    path('vacancies_database/', views.vacancies_database.as_view(), name='vacancies_database'),
    path('logout/',views.logout_view, name='logout'),
]


