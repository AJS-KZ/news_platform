from django.db import models

from utils.models import AbstractUUID, AbstractTimeTracker


class Post(AbstractUUID, AbstractTimeTracker):
    title = models.CharField(
        max_length=500,
        verbose_name='Title'
    )
    link = models.URLField(
        max_length=1000,
        verbose_name='Link'
    )
    votes_count = models.IntegerField(
        default=0,
        verbose_name='Votes Count'
    )
    author = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='Author',
        related_name='posts'
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
