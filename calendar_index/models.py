from django.db import models
from django.contrib.auth.models import User

class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)

class Event(models.Model):
    date_created = models.DateField()
    when = models.DateField(auto_now_add=True)
    description = models.TextField()
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)

class ToDo(models.Model):
    date_created = models.DateField()
    due = models.DateField(auto_now_add=True)
    event = models.ForeignKey(Event, blank=True, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)

class Check_List_Item(models.Model):
    done = models.BooleanField()
    description = models.TextField()
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE)
