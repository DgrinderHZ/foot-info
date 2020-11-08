"""footinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from teams.views import HomePageView, TeamsListView, ScoresListView, TeamDetailView, PlayerDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view()),
    path('teams/', TeamsListView.as_view(), name='teams-list'),
    path('scores/', ScoresListView.as_view(), name='scores-list'),
    path('players/<int:pk>', PlayerDetailView.as_view(), name='player-detail'),
    path('teams/<int:pk>', TeamDetailView.as_view(), name='team-detail')
]
