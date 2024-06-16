"""Module containing URL patterns for the `users` app."""

from django.urls import path
from users.views import users

urlpatterns = [
    path('get-user-info', users.UserView.as_view(), name='fetch-user'),
    path('create-user', users.UserCreateView.as_view(), name='create-user'),
    path('login-user', users.UserLoginView.as_view(), name='login-user'),
    path('ping-view', users.PingView.as_view(), name='ping'),
]
