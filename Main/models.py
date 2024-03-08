from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Calendar(models.Model): #all calendars are stored in this database
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    users = models.ManyToManyField(User, through='UserCalendar')

class Event(models.Model):
    title = models.CharField(max_length=255)
    date_and_time = models.DateTimeField()

    def date(self):
        return self.date_and_time.date()
    
    def time(self):
        return self.date_and_time.time()
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)

class UserCalendar(models.Model): #stores the calendar and the user that created it
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
