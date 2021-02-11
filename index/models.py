from django.db import models
from django.contrib.auth.models import User

class a_dot_user(models.Model):
    user_id = models.CharField(max_length=128)
    user_auth = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id
    