from django.shortcuts import render
from django.http import JsonResponse
from .models import Events

def events_list(request):
    events = Events.objects.all().values('id', 'title', 'author', 'description', 'materials', 'photo', 'date_time', 'places')
    return JsonResponse(list(events), safe=False)

def index(request):
    return render(request, "main/index.html")
