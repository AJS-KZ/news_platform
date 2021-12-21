from django.contrib import admin

from posts.models import Post, Comment


class CommentAdminInLine(admin.StackedInline):
    model = Comment
    extra = 0
    classes = ['collapse']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentAdminInLine,
    ]
