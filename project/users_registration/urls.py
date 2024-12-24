from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.index),  # URL для главной страницы (после регистрации)
    #------------------------------
    # path('register/', views.login_view)
    #----------------------------
]