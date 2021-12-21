from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'uuid',
            'title',
            'link',
            'votes_count',
            'author',
            'created_at',
            'updated_at'
            'comments'
        )


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            'title',
            'link',
            'author',
        )
