from django.shortcuts import render
from django.views import View 
from django.views.generic import ListView, DetailView

from .models import Team, GameScore, Player
# Create your views here.

class HomePageView(View):
    def get(self, request):
        teams = Team.objects.all()
        context = {'teams': teams}
        return render(request, 'teams-list.html', context)

class TeamsListView(ListView):
    model = Team
    template_name = 'teams-list.html'
    context_object_name = 'teams'

class ScoresListView(ListView):
    model = GameScore
    template_name = 'scores-list.html'
    context_object_name = 'scores'

class TeamDetailView(DetailView):
    model = Team
    template_name = 'team-detail.html'
    context_object_name = 'team'

class PlayerDetailView(DetailView):
    model = Player
    template_name = 'player-detail.html'
    context_object_name = 'player'