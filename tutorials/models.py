from django.db import models
from django.contrib.auth.models import User

#NOTE - BASE TUTORIAL MODEL
class BaseTutorial(models.Model):
  """
  Tutorial model, related to "owner" a user instance
  """
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True
    ordering = ["-created_at"]







# SECTION - BASE INHERITED MODELS


class Tutorial(BaseTutorial):
  """
  Tutorial model
  Inherits from TutorialBase:
  "owner",
  "created_at"
  "updated_at"
  """
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tutorial")
  tutorial_title = models.CharField(max_length= 255)
  tutorial_description = models.TextField(blank=True)
  # TODO - Create default image
  preview_art = models.ImageField(
    upload_to="images/", default="../default_post_rgq6aq", blank=True
  )

  def __str__(self):
        return f"{self.id} {self.tutorial_title}"



class TutorialSteps(BaseTutorial):
  """
  Model representing an individual step in a tutorial
  Inherits from TutorialBase:
  "owner",
  "created_at"
  "updated_at"
  """
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tutorial_steps_owner")
  tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name="tutorial_steps")
  step_number = models.PositiveIntegerField()
  step_title = models.CharField(max_length= 255)
  step_content = models.TextField(blank=True)
  step_image = models.ImageField(upload_to="images/", blank=True, null=True)

  class Meta:
    ordering = ["step_number"]

  def __str__(self):
    return f"{self.tutorial} - Step {self.step_number}: {self.step_title}"


class TutorialAttempts(BaseTutorial):
    """
    Model representing an individual attempt at a tutorial
    Inherits from TutorialBase:
    "owner",
    "created_at"
    "updated_at"
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tutorial_attempt_owner")
    tutorial_tried = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name="tutorial_tried")
    submission_image =  models.ImageField(upload_to="images/", blank=True, null=True)
    reflection_text = models.TextField(blank=True)

    def __str__(self):
          return f"{self.owner} tried the {self.tutorial_tried}"


class TutorialFeedback(BaseTutorial):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tutorial__owner")
    tutorial_attempt = models.ForeignKey(TutorialAttempts, on_delete=models.CASCADE, related_name="feedback_entries")
    mentor_feedback = models.TextField(blank=True)

    def __str__(self):
          return f"Feedback by {self.owner}"