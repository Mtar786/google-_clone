from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return super().get_permissions()

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        user = self.get_object()
        if user == request.user:
            return Response(
                {'error': 'You cannot follow yourself'},
                status=status.HTTP_400_BAD_REQUEST
            )
        request.user.following.add(user)
        return Response({'status': 'following'})

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        user = self.get_object()
        request.user.following.remove(user)
        return Response({'status': 'unfollowed'})

    @action(detail=True, methods=['get'])
    def followers(self, request, pk=None):
        user = self.get_object()
        followers = user.followers.all()
        serializer = self.get_serializer(followers, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def following(self, request, pk=None):
        user = self.get_object()
        following = user.following.all()
        serializer = self.get_serializer(following, many=True)
        return Response(serializer.data)