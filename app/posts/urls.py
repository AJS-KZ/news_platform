from rest_framework.routers import DefaultRouter
from django.urls import re_path

from posts.views import PostViewSet, CommentViewSet, VoteViewSet


router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    re_path(r'^vote/(?P<uuid>[0-9a-f]{8}\-[0-9a-f]{4}\-4[0-9a-f]{3}\-[89ab][0-9a-f]{3}\-[0-9a-f]{12})/$',
            VoteViewSet.as_view())
] + router.urls
