from django.urls import path
from .views import analyze,suggest
urlpatterns=[path('analyze/',analyze),path('suggest/',suggest)]
