from django.db import models

from utils.models import AbstractUUID, AbstractTimeTracker


class Vote(AbstractUUID, AbstractTimeTracker):
    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        verbose_name='Post',
        related_name='votes'
    )
    owner = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='Vote Owner',
        related_name='votes'
    )
