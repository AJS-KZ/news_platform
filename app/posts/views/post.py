from django.http import Http404
from rest_framework import viewsets, mixins, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters import rest_framework as filters

from posts.models import Post
from posts.serializers import PostSerializer, PostCreateSerializer
from posts.permissions import PostOwnerOrReadOnly
from posts.filters import PostFilterSet


class PostViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet,):

    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]
    queryset = Post.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilterSet

    def get_permissions(self):
        permission_classes = [AllowAny, ]

        if self.action == 'create':
            permission_classes = [IsAuthenticated, ]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes.append(PostOwnerOrReadOnly)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        serializer_class = PostSerializer

        if self.action == 'create':
            serializer_class = PostCreateSerializer

        return serializer_class

    def list(self, request, *args, **kwargs):
        filtered_queryset = self.filter_queryset(self.queryset.all())
        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_object(self):
        uuid = self.kwargs['pk']
        try:
            instance = self.queryset.get(uuid=uuid)
            return instance
        except:
            raise Http404
