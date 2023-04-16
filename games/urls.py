from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_list, name='main'),
    path('genre/<int:id>', views.games_by_genre, name='genre'),
]