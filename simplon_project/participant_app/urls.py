
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.signup_participant),
    path('list-participant/', views.view_list)

]