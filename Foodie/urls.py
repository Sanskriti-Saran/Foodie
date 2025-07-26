from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),
    path('veg/', views.veg_spots, name='veg'),
    path('nonveg/', views.non_veg_spots, name='nonveg'),
    path('meals/', views.full_course_spots, name='meals'),
    path('desserts/', views.dessert_spots, name='desserts'),
    path('about/', lambda request: render(request, 'about.html'), name='about'),
]
