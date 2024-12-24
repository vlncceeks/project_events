from django.shortcuts import render

from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.http import HttpResponseRedirect

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
#------------------------------
def login_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        
        usr = authenticate(request, username=login, password=password)
        if usr is not None:
            user_login(request, usr)
            return HttpResponseRedirect('/')
        else:
            return render(request, template_name='auth/registration.html')

    return render(request, template_name='auth/registration.html')

#--------------------