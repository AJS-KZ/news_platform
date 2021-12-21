from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import CustomUser
from users.serializers import CustomUserSerializer


class CustomUserViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
