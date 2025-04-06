from django.db import models
from django.conf import settings

class Circle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_circles')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='circles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name