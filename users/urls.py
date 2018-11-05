#! /usr/bin/env python
__author__ = 'Cindalis Cepero'

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name = 'signup'),
]