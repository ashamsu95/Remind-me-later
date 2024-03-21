from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    reminder_time = models.DateTimeField()
    reminder_method = models.CharField(max_length=10, choices=[('email', 'Email'), ('sms', 'SMS')])



