from django.conf import settings
from django.db import models
from django.utils import timezone


def photo_upload_path(instance: "Thought", filename: str) -> str:
    return f"photos/{filename}"


class Thought(models.Model):
    """A single thought shared to the feed."""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="thoughts",
    )
    display_name = models.CharField(max_length=50, default="Anonymous")
    body = models.TextField()
    photo = models.ImageField(upload_to=photo_upload_path, blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.display_name}: {self.body[:40]}"

    @property
    def comment_count(self) -> int:
        return self.comments.count()


class Comment(models.Model):
    """A simple threaded comment for a thought."""

    thought = models.ForeignKey(
        Thought, on_delete=models.CASCADE, related_name="comments"
    )
    author_name = models.CharField(max_length=50, default="Anonymous")
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"{self.author_name} on {self.thought}"

