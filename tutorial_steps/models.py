from django.db import models
from django.contrib.auth.models import User
from tutorials.models import Tutorial

# Create your models here.

class TutorialSteps(models.Model):
  """
  Model representing an individual step in a tutorial
  """
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name="tutorial_steps")
  step_number = models.PositiveIntegerField()
  step_title = models.CharField(max_length= 255)
  step_content = models.TextField(blank=True)
  step_image = models.ImageField(upload_to="images/", blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ["step_number"]

  def __str__(self):
    return f"{self.tutorial} - Step {self.step_number}: {self.step_title}"