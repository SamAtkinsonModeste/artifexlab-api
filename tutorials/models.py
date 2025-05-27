from django.db import models
from django.contrib.auth.models import User

class Tutorial(models.Model):
  """
  Tutorial model, related to "owner" a user instance
  """

  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  tutorial_title = models.CharField(max_length= 255)
  tutorial_description = models.TextField(blank=True)
  # TODO - Create default image
  preview_art = models.ImageField(
    upload_to="images/", default="../default_post_rgq6aq", blank=True
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ["-created_at"]

  def __str__(self):
        return f"{self.id} {self.tutorial_title}"
