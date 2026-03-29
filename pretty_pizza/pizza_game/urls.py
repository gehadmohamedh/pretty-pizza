from django.urls import path
from .views import pizza_game

urlpatterns = [
    path('', pizza_game, name='pizza_game'),
]