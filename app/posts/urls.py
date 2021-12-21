from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet


router = DefaultRouter()

router.register('', PostViewSet)

urlpatterns = [] + router.urls
