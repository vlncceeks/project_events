from django.db import models

class Events(models.Model):
    title = models.CharField('Название', max_length=250)
    author = models.CharField('автор', max_length=250)
    description = models.TextField('Описание')
    materials = models.TextField('Материлы')
    photo = models.ImageField(upload_to='images/')
    date_time = models.DateTimeField('Дата мероприятия')
    places = models.IntegerField('Всего мест')

    def __str__(self):
        return self.title