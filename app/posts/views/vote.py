from django.http import Http404
from rest_framework import viewsets, mixins, status, views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters import rest_framework as filters

from posts.models import Vote
from posts.serializers import VoteSerializer


class VoteViewSet(views.APIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        if 'uuid' in kwargs.keys():
            try:
                serializer = self.serializer_class(self.queryset.get(pk=kwargs['uuid']))
                response = serializer.data
            except Exception:
                raise Http404
        else:
            response = self.serializer_class(self.queryset.all(), many=True).data

        return Response(data=response, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request_kwargs': kwargs, 'request': request})
        serializer.is_valid()
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        if 'uuid' in kwargs.keys():
            try:
                serializer = self.serializer_class().__delete__(self.queryset.get(pk=kwargs['uuid']))
                return Response(data={'details': serializer}, status=status.HTTP_200_OK)
            except Exception:
                raise ValidationError("Any Vote with given UUID Not Found!")
        else:
            raise ValidationError("Vote UUID Not Found!")
