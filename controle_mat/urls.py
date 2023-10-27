from django.contrib import admin
from django.urls import path, include
from .views import index, createStudent, editStudent, deleteStudent, showStudent

urlpatterns = [
    path('', index, name="index"),
    path('createStudent', createStudent, name="createStudent"),
    path('showStudent/<int:id>', showStudent, name='showStudent'),
    path('editStudent/<int:id>', editStudent, name='editStudent'),
    path('deleteStudent/<int:id>', deleteStudent, name='deleteStudent'),
]