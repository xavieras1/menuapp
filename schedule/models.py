from django.contrib.auth.models import User
from django.db import models

from meal.models import Meal

class Schedule(models.Model):
    user = models.ForeignKey(User, related_name='schedules', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.id

class ScheduleItem(models.Model):
    list = models.ForeignKey(Schedule, related_name='meals', on_delete=models.CASCADE)
    product = models.ForeignKey(Meal, related_name='meals', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    person = models.CharField(max_length=100)
    shift = models.CharField(max_length=100)
    day = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % self.id