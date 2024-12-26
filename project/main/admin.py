from django.contrib import admin

from .models import Events

admin.site.register(Events)

from .models import EventParticipant

class EventParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registered_at')  # Список полей, которые будут отображаться в админке
    search_fields = ('user__username', 'event__title')  # Поиск по пользователю и мероприятию

admin.site.register(EventParticipant, EventParticipantAdmin)

