from django.db import models

class Users(models.Model):
    login = models.CharField('Логин', max_length=250)
    email = models.EmailField('Email', max_length=250)
    password = models.CharField('Пароль', max_length=250)

    def __str__(self):
        return self.login

