from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from posts.models import Vote, Post


class VoteSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Vote
        fields = ('post', 'owner')

    def validate(self, attrs):
        if 'request_kwargs' in self.context.keys():
            request_kwargs = self.context['request_kwargs']
            if 'uuid' in request_kwargs.keys():
                uuid = request_kwargs['uuid']
                post = Post.objects.filter(pk=uuid).first()
                if post:
                    attrs['post'] = post
                else:
                    raise ValidationError("Any Post with this UUID Not Found!")
            else:
                raise ValidationError("Post's UUID Not Found!")

        if 'request' in self.context.keys():
            attrs['user'] = self.context['request'].user
        else:
            raise ValidationError("Couldn't Find User Info!")

        return attrs

    def create(self, validated_data):
        instance = Vote.objects.create(post=validated_data['post'], owner=validated_data['user'])
        post = validated_data['post']
        post.votes_count += 1
        post.save()

        return instance

    def __delete__(self, instance):
        post = instance.post
        post.votes_count -= 1
        post.save()
        instance.delete()

        return 'Vote Deleted!'
