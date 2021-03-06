from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    major = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    image = models.ImageField(default='default-new.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.email

  
