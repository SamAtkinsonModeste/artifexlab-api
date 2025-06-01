from rest_framework import serializers
from .models import Tutorial, TutorialSteps, TutorialAttempts, TutorialFeedback
from likes.models import LikeTutorial

class BaseTutorialSerializer(serializers.ModelSerializer):
  """
    Base serializer to include shared fields and logic:
    - owner username
    - is_owner check
    - created_at and updated_at timestamps
    """
  owner = serializers.ReadOnlyField(source="owner.username")
  is_owner = serializers.SerializerMethodField()

  def get_is_owner(self, obj):
    request = self.context["request"]
    return request.user == obj.owner


  class Meta:
    abstract = True
    fields = [
            "id",
            "owner",
            "is_owner",
            "created_at",
            "updated_at",
    ]



class TutorialSerializer(BaseTutorialSerializer, serializers.ModelSerializer):
  """
    Full serializer for the Tutorial model.
    Includes:
    - profile info
    - related tutorial steps (first step title preview)
    - like/comment counts
    - current user's like ID (if it exists)
    """
  profile_id = serializers.ReadOnlyField(source="owner.profile.id")
  profile_image = serializers.ReadOnlyField(source="owner.profile_image.image.url")
  tutorial_steps = serializers.SerializerMethodField()
  tutorial_steps_titles = serializers.SerializerMethodField()
  tutorial_likes_id = serializers.SerializerMethodField()
  tutorial_likes_count = serializers.ReadOnlyField()
  tutorial_comments_count = serializers.ReadOnlyField()

  def validate_preview_art(self, value):
        """
        Validate the image field to ensure it is not too:
        - large (2MB)
        - wide (4096px)
        - tall (4096px)
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError("Image size cannot exceed 2MB!")
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width cannot exceed 4096px!"
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height cannot exceed 4096px!"
            )

        return value


  def get_tutorial_steps(self,obj):
     """
    Returns the title of the first step in the tutorial,
    ordered by step_number. Used for preview purposes.
    """
     step_num = obj.tutorial_steps.order_by("step_number").count()
     return step_num if step_num else None

  def get_tutorial_steps_titles(self,obj):
     """
    Returns the title of the first step in the tutorial,
    ordered by step_number. Used for preview purposes.
    """
     step_title = obj.tutorial_steps.order_by("step_number").values_list("step_title", flat=True)
     return step_title if step_title else None





  def get_tutorial_likes_id(self, obj):
        """
    Returns the ID of the LikeTutorial instance for the current user,
    if it exists. Used to check whether the tutorial is liked by the user.
    """
        user = self.context["request"].user
        if user.is_authenticated:
            tutorial_likes = LikeTutorial.objects.filter(owner=user, tutorial=obj).first()
            return tutorial_likes.id if tutorial_likes else None
        return None



  class Meta:
    model = Tutorial
    fields = BaseTutorialSerializer.Meta.fields + [
            "profile_id",
            "profile_image",
            "tutorial_title",
            "tutorial_description",
            "tutorial_steps",
             "tutorial_steps_titles",
            "preview_art",
            "tutorial_likes_id",
            "tutorial_comments_count",
            "tutorial_likes_count",
    ]


class TutorialStepsSerializer(BaseTutorialSerializer,serializers.ModelSerializer):
  """
    Serializer for individual tutorial steps.
    Includes tutorial link, step number, title, content, and optional image.
    """
  tutorial_title = serializers.ReadOnlyField(source="tutorial.tutorial_title")

  class Meta:
      model = TutorialSteps
      fields = BaseTutorialSerializer.Meta.fields + [
         "tutorial",
         "tutorial_title",
         "step_number",
         "step_title",
         "step_content",
         "step_image",
      ]


class TutorialAttemptsSerializer(BaseTutorialSerializer,serializers.ModelSerializer):
  """
    Serializer for user-submitted tutorial attempts.
    Includes submitted image and personal reflection.
    """

  class Meta:
      model = TutorialAttempts
      fields = BaseTutorialSerializer.Meta.fields + [
         "tutorial_try",
         "submission_image",
         "reflection_text",
      ]


class TutorialFeedbackSerializer(BaseTutorialSerializer,serializers.ModelSerializer):
  """
    Serializer for feedback on tutorial attempts.
    Intended to be used by the tutorial owner (mentor).
    """

  class Meta:
      model = TutorialFeedback
      fields = BaseTutorialSerializer.Meta.fields + [
         "tutorial_attempt",
         "mentor_feedback",

      ]