from django.contrib.auth.models import User
from django.db import models

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, unique=True)

    class Meta:
        unique_together = ('user', 'phone_number')

    def __str__(self):
        return self.user.username