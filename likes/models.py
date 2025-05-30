from django.db import models
from django.contrib.auth.models import User
from artworks.models import Artwork
from tutorials.models import Tutorial
# from tutorials.models import TutorialAttempt

# Create your models here.


class LikeBase(models.Model):
    """
    Abstract Base class with the common fields
    to be used for all the Like models
    For each model class the field name and values for:
    ForeignKey
    related_name
    will be unique
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]







class LikeArtwork(LikeBase):
    """
    Like model for Artwork content.
    Inherits from LikeBase
    """
    artwork =models.ForeignKey(Artwork, on_delete=models.CASCADE,related_name="artwork_likes" )

def __str__(self):
    return f"{self.owner.username} liked {self.artwork.title}"




class LikeTutorial(LikeBase):
    """
    Like model for Tutorial content.
    Inherits from LikeBase
    """
    tutorial =models.ForeignKey(Tutorial, on_delete=models.CASCADE,related_name="tutorial_likes" )

    class Meta:
        unique_together = ("owner", "tutorial")

    def __str__(self):
        return f"{self.owner.username} liked {self.tutorial.title}"







