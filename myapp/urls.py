from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('generate_report_pdf/', views.generate_report_pdf, name='generate_report_pdf'),
   
]
