from django.db import models
from django.contrib.auth.models import User
from artworks.models import Artwork


class Comment(models.Model):
    """
    Comment model, related to User and Artwork
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
     return self.content[:50] + ("..." if len(self.content) > 50 else "")
