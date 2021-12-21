from django.urls import re_path, path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet


router = DefaultRouter()
router.register('', CustomUserViewSet)

urlpatterns = [

] + router.urls
