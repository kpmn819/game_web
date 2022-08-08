# refers to the views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('v1/', views.v1, name='view 1'),
    path('home/', views.home, name='home')
]