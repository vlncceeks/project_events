from django.shortcuts import render

def register(request):
    return render(request, 'users_registration/registration.html')