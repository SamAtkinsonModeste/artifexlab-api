from django.db import models
from django.contrib.auth.models import User
from artworks.models import Artwork

# Create your models here.


class Like(models.Model):
    """
    Like model, related to 'owner' and 'artwork'.
    'owner' is a User instance and 'artwork' is a Artwork instance.
    'unique_together' makes sure a user can't like the same artwork twice.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ForeignKey(
        Artwork, related_name="likes", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("owner", "artwork")

    def __str__(self):
        return f"{self.owner.username} liked {self.artwork.title}"
