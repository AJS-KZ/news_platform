from django.contrib import admin

from posts.models import Post, Comment, Vote


class CommentAdminInLine(admin.StackedInline):
    model = Comment
    extra = 0
    classes = ['collapse']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentAdminInLine,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
