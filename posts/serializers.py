from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import UserSerializer
from circles.serializers import CircleSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'created_at',
                 'updated_at', 'likes_count', 'is_liked')
        read_only_fields = ('id', 'author', 'created_at', 'updated_at')

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return user in obj.likes.all()

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    circles = CircleSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'content', 'image', 'created_at',
                 'updated_at', 'likes_count', 'comments_count',
                 'is_liked', 'comments', 'circles', 'is_public')
        read_only_fields = ('id', 'author', 'created_at', 'updated_at')

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return user in obj.likes.all()

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('content', 'image', 'circles', 'is_public')

    def create(self, validated_data):
        circles = validated_data.pop('circles', [])
        post = Post.objects.create(author=self.context['request'].user, **validated_data)
        post.circles.set(circles)
        return post

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('content', 'image', 'circles', 'is_public')