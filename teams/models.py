from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=256, unique=True)
    details = models.TextField()

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=256)
    number = models.IntegerField()
    age = models.IntegerField()
    position = models.CharField(max_length=256, choices=(('1', 'حارس'), ('2', 'دفاع'), ('3', 'وسط'), ('4', 'هجوم')))
    is_captain = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class GameScore(models.Model):
    first_team = models.CharField(max_length=256)
    second_team = models.CharField(max_length=256)
    first_team_score = models.IntegerField(default=0)
    second_team_score = models.IntegerField(default=0)

    def __str__(self):
        return '{} {} - {} {}'.format(self.first_team, 
                                      self.first_team_score, 
                                      self.second_team_score,
                                      self.second_team)


