# Generated by Django 5.1.4 on 2024-12-24 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=250, verbose_name='Логин')),
                ('email', models.EmailField(max_length=250, verbose_name='Email')),
                ('password', models.CharField(max_length=250, verbose_name='Пароль')),
            ],
        ),
    ]
