from django.contrib import admin
from django.urls import path
from .views import about_page, about_details

urlpatterns = [
    path("", about_page, name="about"),
    path('details/', about_details , name="about-details"),
   
]