from django.shortcuts import render


from rest_framework.generics import ListAPIView
from .models import Events
from .serializers import EventSerializer
from rest_framework import filters

class EventListView(ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']  # Поле, по которому будет происходить поиск



def index(request):
    return render(request, "main/index.html")

