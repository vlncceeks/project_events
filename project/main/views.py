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

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import EventParticipant, Events

@login_required
def register_for_event(request, event_id):
    event = Events.objects.get(id=event_id)

    # Проверяем, доступно ли место
    if event.total_seats > 0:
        # Проверяем, не записан ли пользователь уже на это мероприятие
        if EventParticipant.objects.filter(user=request.user, event=event).exists():
            return JsonResponse({"error": "Вы уже записаны на это мероприятие"}, status=400)

        # Записываем пользователя
        EventParticipant.objects.create(user=request.user, event=event)

        # Уменьшаем количество доступных мест в базе данных
        event.available_seats -= 1
        event.save()

        # Возвращаем обновленные данные о количестве мест
        return JsonResponse({
            "message": "Вы успешно записаны на мероприятие!",
            "available_seats": event.available_seats
        })

    else:
        return JsonResponse({"error": "Нет доступных мест"}, status=400)
