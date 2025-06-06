from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Artwork(models.Model):
    """
    Artwork model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """


    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="artworks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/", default="../default_post_rgq6aq", blank=True
    )


    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"
