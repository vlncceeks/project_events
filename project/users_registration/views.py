# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# from django.contrib.auth import authenticate, login as user_login, logout as user_logout
# from django.http import HttpResponseRedirect


# @login_required
# def register(request):
#     return render(request, 'users_registration/registration.html')

#------------------------------
# def login_view(request):
#     if request.method == 'POST':
#         login = request.POST.get('login')
#         password = request.POST.get('password')
        
#         usr = authenticate(request, username=login, password=password)
#         if usr is not None:
#             user_login(request, usr)
#             return HttpResponseRedirect('/')
#         else:
#             return render(request, template_name='register/registration.html')

#     return render(request, template_name='register/registration.html')

#--------------------

from django.shortcuts import render, HttpResponsePermanentRedirect
from users_registration.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth  
from django.urls import reverse


def index(request):
    return render(request, "main/index.html")
    
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return(HttpResponsePermanentRedirect("/"))
                
    else:
        form = UserLoginForm()
    
    context = {'form': form}
    return render(request, 'users_registration/login.html', context)

def register(request):
    if request.method =="POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
            
    context = {'form': form}
    return render(request, 'users_registration/registration.html', context)