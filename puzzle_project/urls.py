"""
URL configuration for puzzle_project project.
"""
from django.urls import path, include

urlpatterns = [
    path('', include('puzzle_app.urls')),
]
