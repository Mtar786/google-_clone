from rest_framework import serializers
from .models import Circle
from accounts.serializers import UserSerializer

class CircleSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    member_count = serializers.SerializerMethodField()

    class Meta:
        model = Circle
        fields = ('id', 'name', 'description', 'creator', 'members',
                 'member_count', 'created_at', 'updated_at', 'is_private')
        read_only_fields = ('id', 'creator', 'created_at', 'updated_at')

    def get_member_count(self, obj):
        return obj.members.count()

class CircleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circle
        fields = ('name', 'description', 'is_private')

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        circle = Circle.objects.create(**validated_data)
        circle.members.add(self.context['request'].user)
        return circle

class CircleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circle
        fields = ('name', 'description', 'is_private')