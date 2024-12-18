from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/events/', views.events_list, name='events_list'),
]