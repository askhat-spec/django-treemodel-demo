from django.shortcuts import render
from .models import Game


def games_by_genre(request, id):
    games = Game.objects.filter(genres__id=id)
    return render(request, 'home.html', {'games': games})


def games_list(request):
    games = Game.objects.all()
    return render(request, 'home.html', {'games': games})
