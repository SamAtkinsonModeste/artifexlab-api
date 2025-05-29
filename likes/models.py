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
    For each model class the values for:
    ForeignKey
    related_name
    {self.content.title}
    will be unique
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="%(app_label)s_%(class)s_likes", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
        unique_together = ("owner", "content")


    def __str__(self):
        return f"{self.owner.username} liked {self.content.title}"



class LikeArtwork(LikeBase):
    """
    Like model for Artwork content.
    Inherits from LikeBase
    """
    content =models.ForeignKey(Artwork, related_name="artwork_likes", on_delete=models.CASCADE)




class LikeTutorial(LikeBase):
    """
    Like model for Tutorial content.
    Inherits from LikeBase
    """
    content =models.ForeignKey(Tutorial, related_name="tutorial_likes", on_delete=models.CASCADE)







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
