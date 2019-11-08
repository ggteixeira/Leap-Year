from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addYear, name='addYear' ),
    path('calculate/<pk>', views.calculate, name='calculate'),
]

