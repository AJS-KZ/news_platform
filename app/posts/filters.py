from django_filters import rest_framework as filters

from posts.models import Post


class PostFilterSet(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='contains')
    link = filters.CharFilter(field_name='link', lookup_expr='contains')
    votes = filters.NumberFilter(field_name='votes', lookup_expr='gt')

    class Meta:
        model = Post
        fields = ('title', 'link', 'votes', 'author')
