"""Module containing URL patterns for the `users` app."""

from django.urls import path
from users.views import users

urlpatterns = [
    path('create-user', users.UserCreateView.as_view(), name='create-user'),
    path('login-user', users.UserLoginView.as_view(), name='create-user'),
]
