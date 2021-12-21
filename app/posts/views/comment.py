from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from posts.models import Comment
from posts.serializers import CommentSerializer, CommentCreateSerializer, CommentUpdateSerializer
from posts.permissions import CommentOwnerOrReadOnly, CommentDeletePermission


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet,):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny, ]
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        serializer_class = CommentSerializer

        if self.action == 'create':
            serializer_class = CommentCreateSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            serializer_class = CommentUpdateSerializer

        return serializer_class

    def get_permissions(self):
        permission_classes = [IsAuthenticated, ]

        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny, ]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes.append(CommentOwnerOrReadOnly)
        elif self.action == 'destroy':
            permission_classes.append(CommentDeletePermission)

        return [permission() for permission in permission_classes]
