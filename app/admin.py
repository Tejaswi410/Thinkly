from django.contrib import admin
from .models import Thought, Comment


@admin.register(Thought)
class ThoughtAdmin(admin.ModelAdmin):
    list_display = ("display_name", "created_at", "likes")
    search_fields = ("display_name", "body")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author_name", "thought", "created_at")
    search_fields = ("author_name", "body")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)

