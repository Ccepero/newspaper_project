#! /usr/bin/env python
__author__ = 'Cindalis Cepero'

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]