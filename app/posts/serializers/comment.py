from rest_framework import serializers

from posts.models import Comment
from users.serializers import CustomUserAuthorSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = CustomUserAuthorSerializer()

    class Meta:
        model = Comment
        fields = (
            'uuid',
            'content',
            'post',
            'author'
        )


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('content', 'post', 'author')


class CommentUpdateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('content', 'author')
