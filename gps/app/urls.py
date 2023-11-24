# En app/urls.py

from django.urls import path
from .views import map_view, receive_gps

urlpatterns = [
    path('', map_view, name='map_view'),  # path('', map_view, name='map_view'),
    path('receive_gps/', receive_gps, name='receive_gps'),
]
