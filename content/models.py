
from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    video_slug = models.SlugField()
    
class Session(models.Model):
    exercise = models.ForeignKey(Exercise, related_name="exercise_type", on_delete=models.CASCADE)
    sets = models.IntegerField()
    rep_count = models.IntegerField()
    working_weight = models.IntegerField()
    pr_weight = models.IntegerField()
    
    
    
