
from django.urls import path

from money import views

urlpatterns = [

    path('', views.index),
    ]
