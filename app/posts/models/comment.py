from django.db import models

from utils.models import AbstractUUID, AbstractTimeTracker


class Comment(AbstractUUID, AbstractTimeTracker):
    content = models.CharField(
        max_length=500,
        verbose_name='Comment Text'
    )
    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        verbose_name='Post',
        related_name='comments'
    )
    author = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='Comment Owner',
        related_name='comments'
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
