from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='Register'),
    path('login/', views.UserLoginView.as_view(), name='Login'),
    path('logout/', views.UserLogoutView.as_view(), name='Logout')
]