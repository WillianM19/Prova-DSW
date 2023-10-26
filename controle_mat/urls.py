from django.contrib import admin
from django.urls import path, include
from .views import index, createStudent

urlpatterns = [
    path('', index, name="index"),
    path('createStudent/', createStudent, name="createStudent")
]