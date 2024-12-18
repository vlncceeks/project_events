from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('api/events/', views.events_list, name='events_list'),
]

from .views import EventListView

urlpatterns += [
    path('api/events/', EventListView.as_view(), name='event-list'),
]

