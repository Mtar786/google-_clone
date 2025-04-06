from rest_framework import serializers
from .models import Notification
from accounts.serializers import UserSerializer
from posts.serializers import PostSerializer, CommentSerializer
from circles.serializers import CircleSerializer

class NotificationSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    comment = CommentSerializer(read_only=True)
    circle = CircleSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ('id', 'recipient', 'sender', 'notification_type',
                 'post', 'comment', 'circle', 'created_at', 'is_read')
        read_only_fields = ('id', 'recipient', 'sender', 'created_at')