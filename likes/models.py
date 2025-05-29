from django.db import models
from django.conf import settings
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







# class LikeTutorial(models.Model):
#     """
#     Like model, related to 'owner' and 'tutorials'.
#     'owner' is a User instance and 'tutorial' is a Tutorial instance.
#     'unique_together' makes sure a user can't like the same tutorial twice.
#     """

#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     tutorial = models.ForeignKey(
#         Tutorial, related_name="tutorial_likes", on_delete=models.CASCADE
#     )
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["-created_at"]
#         unique_together = ("owner", "tutorial")

#     def __str__(self):
#         return f"{self.owner.username} liked {self.tutorial.title}"




# class LikeTutorialAttempts(models.Model):
#     """
#     Like model, related to 'owner' and 'tutorial attempts'.
#     'owner' is a User instance and 'tutorial attempts' is a TutorialAttempt instance.
#     'unique_together' makes sure a user can't like the same tutorial attempt twice.
#     """

#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     tutorial_attempt = models.ForeignKey(
#         TutorialAttempt, related_name="likes", on_delete=models.CASCADE
#     )
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["-created_at"]
#         unique_together = ("owner", "tutorial")

#     def __str__(self):
#         return f"{self.owner.username} liked {self.tutorial.title}"
