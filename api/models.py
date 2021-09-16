from django.contrib.auth.models import User
from django.db import models


class Report(models.Model):
    ACTIVITIES = (
        ('Walking', 'Walking'),
        ('Running', 'Running'),
        ('Bike', 'Bike'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    start_activity = models.DateTimeField(null=True, blank=True)
    end_activity = models.DateTimeField(null=True, blank=True)
    activity = models.CharField(max_length=200, choices=ACTIVITIES, null=True)
    distance = models.FloatField()
    calories = models.FloatField()