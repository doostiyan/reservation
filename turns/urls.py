from django.urls import path

from turns.views import home

urlpatterns = [
    path('h/', home),
]