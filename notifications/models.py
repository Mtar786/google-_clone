from django.db import models
from django.conf import settings

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
        ('circle_invite', 'Circle Invite'),
        ('circle_join', 'Circle Join'),
    )

    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey('posts.Comment', on_delete=models.CASCADE, null=True, blank=True)
    circle = models.ForeignKey('circles.Circle', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.sender.username} {self.notification_type} notification for {self.recipient.username}"