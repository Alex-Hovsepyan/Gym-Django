from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('team', views.team, name='team'),
    path('classes/<slug:slug>/', views.classes, name='classes'),
    path('gallery', views.gallery, name='gallery'),
    path('bmi', views.bmi, name='bmi'),
    path('contact', views.contact, name='contact'),
]