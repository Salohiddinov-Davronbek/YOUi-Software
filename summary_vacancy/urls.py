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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from summary_vacancy import views

from django.conf import settings
from django.conf.urls.static import static
app_name = "summary_vacancy"

urlpatterns = [
    path('', views.home, name='home'),
    path('vac_search/', views.vac_search, name='vac_search'),
    path('res_search/', views.res_search, name='res_search'),
    path('vacancies_create/', views.vacancies_create.as_view(), name='vacancies_create'),
    path('v_profile/', views.vacancies_profile, name='v_profile'),
    path('v_details/', views.vacancies_profile_dataile, name='v_details'),
    path('company_vacancy_create/', views.company_vacancy_create, name='company_vacancy_create'),
    path('my_vacansies/', views.my_vacansies, name='my_vacansies'),
    path('vacancies_biografies/', views.vacancies_biografies, name='vacancies_biografies'),
    path('resume<int:id>/', views.res_vac_detail, name='res_vac_detail'),
    path('vacancy<int:id>/', views.vac_res_detail, name='vac_res_detail'),


    path('user_profile/', views.user_profile, name='user_profile'),
        
    path('summary_create/', views.summary_create.as_view(), name='summary_create'),
    path('login/', views.summary_vacancies_login, name='login'),
    path('s_profile/', views.summary_profile, name='s_profile'),
    path('s_details/', views.summary_profile_dataile, name='s_details'),
    path('editt/<int:pk>/', views.summary_image_uplo, name='book_editt'),


    path('meine_biografiess/', views.meine_biografies, name="meine_biografiess"),
    path('create_resume/', views.create_resume, name='create_resume'),

    # path('edit/<int:pk>/', views.book_update, name='book_edit'),
    path('edit/<int:pk>/', views.book_update, name='book_edit'),

    path('delete/<int:pk>/', views.resume_deldf, name='resume_delete'),




]

