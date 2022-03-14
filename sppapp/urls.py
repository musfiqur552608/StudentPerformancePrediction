from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('studentperformance', views.studentperformance, name='studentperformance'),
    # path('test', views.test, name='test'),
]