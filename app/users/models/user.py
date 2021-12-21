from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractUUID, AbstractTimeTracker
from users.managers import CustomUserManager
from utils.const import UserKind


class CustomUser(AbstractBaseUser, PermissionsMixin, AbstractUUID, AbstractTimeTracker):
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name='email'
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name='first_name'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='last_name'
    )
    avatar = models.ImageField(
        upload_to='uploads/avatars/',
        blank=True,
        null=True
    )
    kind = models.CharField(
        choices=UserKind.choice(),
        default=UserKind.USER.value,
        max_length=6,
        verbose_name=_('kind')
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('uuid', )

    def __str__(self):
        return self.email+" "+self.first_name+" "+self.last_name
