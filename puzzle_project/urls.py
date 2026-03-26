"""
URL configuration for puzzle_project project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('puzzle_app.urls')),
]
