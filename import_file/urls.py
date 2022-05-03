# from rest_framework.authtoken import views
from django.urls import path

from .views import ImportCSV

urlpatterns = [
    path('csv/', ImportCSV.as_view()),
]