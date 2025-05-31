from django.db import models
from django.contrib.auth.models import User

class Tutorial(models.Model):
  """
  Tutorial model, related to "owner" a user instance
  """

  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tutorial")
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



class TutorialSteps(models.Model):
  """
  Model representing an individual step in a tutorial
  """
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name="tutorial_steps")
  step_number = models.PositiveIntegerField()
  step_title = models.CharField(max_length= 255)
  step_content = models.TextField(blank=True)
  step_image = models.ImageField(upload_to="images/", blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ["step_number"]

  def __str__(self):
    return f"{self.tutorial} - Step {self.step_number}: {self.step_title}"


class TutorialAttempts(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tutorial_try = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name="tutorial_tried")
    image =  models.ImageField(upload_to="images/", blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering  = ["-created_at"]

    def __str__(self):
          return f"{self.owner} tried the {self.tutorial_try}"


class TutorialFeedback(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tutorial_attempt = models.ForeignKey(TutorialAttempts, on_delete=models.CASCADE, related_name="tutorial_attempt")
    feedback = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering  = ["-created_at"]

    def __str__(self):
          return f"{self.owner}"