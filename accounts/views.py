from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from accounts.forms import RegisterForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('Home')


    

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

class UserLogoutView(LogoutView):
    model = User
    next_page = 'Home'
    