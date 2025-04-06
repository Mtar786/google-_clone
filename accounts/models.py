from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='cover_photos/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=200, blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    def __str__(self):
        return self.username