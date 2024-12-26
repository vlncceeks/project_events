from django.db import models

class Events(models.Model):
    title = models.CharField('Название', max_length=250)
    author = models.CharField('автор', max_length=250)
    description = models.TextField('Описание')
    materials = models.TextField('Материлы')
    photo = models.ImageField(upload_to='images/')
    date_time = models.DateTimeField('Дата мероприятия')
    places = models.IntegerField('Всего мест')
    total_seats = models.PositiveIntegerField('свободные места', default=0)
    available_seats = models.PositiveIntegerField('*', default=0)  # Это будет использоваться только для отображения

    def __str__(self):
        return self.title
    

from django.db import models
from django.contrib.auth.models import User
# from .events import Events  # Подключите модель Events, если она в другом файле

class EventParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, который записался
    event = models.ForeignKey(Events, on_delete=models.CASCADE)  # Мероприятие, на которое записан пользователь
    registered_at = models.DateTimeField(auto_now_add=True)  # Время регистрации

    def __str__(self):
        return f"{self.user.username} зарегистрирован на {self.event.title}"
