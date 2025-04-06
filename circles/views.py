from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Circle
from .serializers import CircleSerializer, CircleCreateSerializer, CircleUpdateSerializer

class CircleViewSet(viewsets.ModelViewSet):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return CircleCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return CircleUpdateSerializer
        return CircleSerializer

    def get_queryset(self):
        user = self.request.user
        return Circle.objects.filter(members=user)

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        circle = self.get_object()
        if circle.is_private:
            return Response(
                {'error': 'This circle is private'},
                status=status.HTTP_403_FORBIDDEN
            )
        circle.members.add(request.user)
        return Response({'status': 'joined circle'})

    @action(detail=True, methods=['post'])
    def leave(self, request, pk=None):
        circle = self.get_object()
        if circle.creator == request.user:
            return Response(
                {'error': 'Creator cannot leave the circle'},
                status=status.HTTP_400_BAD_REQUEST
            )
        circle.members.remove(request.user)
        return Response({'status': 'left circle'})

    @action(detail=True, methods=['post'])
    def invite(self, request, pk=None):
        circle = self.get_object()
        if circle.creator != request.user:
            return Response(
                {'error': 'Only creator can invite members'},
                status=status.HTTP_403_FORBIDDEN
            )
        user_id = request.data.get('user_id')
        if not user_id:
            return Response(
                {'error': 'user_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = get_object_or_404(User, id=user_id)
        circle.members.add(user)
        return Response({'status': 'user invited'})