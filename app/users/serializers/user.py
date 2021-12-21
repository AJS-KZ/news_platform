from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserAuthorSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('uuid', 'email', 'first_name', 'last_name')
