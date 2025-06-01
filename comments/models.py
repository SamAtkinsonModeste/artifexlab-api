from django.db import models
from django.contrib.auth.models import User
from artworks.models import Artwork
from tutorials.models import Tutorial, TutorialAttempts

class CommentBase(models.Model):
    """
    Comment model, related to User and Artwork
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
     return self.content[:50] + ("..." if len(self.content) > 50 else "")


class CommentArtwork(CommentBase):
   """
    Comment model for Artwork content.
    Inherits from CommentBase
    Deletes comment if related artwork is deleted.
    """
   artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name="artwork_comments")

class CommentTutorial(CommentBase):
   """
    Comment model for Tutorial content.
    Inherits from CommentBase
    Deletes comment if related Tutorial is deleted.
    """
   tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name="tutorial_comments")


class CommentTutorialAttempts(CommentBase):
    """
    Comment model for Tutorial Attempts content.
    Inherits from CommentBase
    Deletes comment if related Tutorial Attempt is deleted.
    """
    tutorial_attempts = models.ForeignKey(TutorialAttempts, on_delete=models.CASCADE, related_name="tutorial_attempts_comments")