from django.shortcuts import render
from django.views import View

from .models import *
# Create your views here.

class HomePageView(View):
    def get(self, request):
        teams = Team.objects.all()
        context = {'teams': teams}
        return render(request, 'teams-list.html', context)


