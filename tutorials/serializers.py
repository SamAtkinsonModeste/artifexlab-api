from rest_framework import serializers
from .models import Tutorial
from likes.models import LikeTutorial
from tutorial_steps.serializers import TutorialStepsSerializer

class TutorialSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source="owner.username")
  is_owner = serializers.SerializerMethodField()
  profile_id = serializers.ReadOnlyField(source="owner.profile.id")
  profile_image = serializers.ReadOnlyField(source="owner.profile_image.image.url")
  tutorial_steps = serializers.SerializerMethodField()
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





  def get_is_owner(self, obj):
    request = self.context["request"]
    return request.user == obj.owner

  def get_tutorial_steps(self, obj):
      steps = obj.tutorial_steps.all().order_by("step_number")
      return TutorialStepsSerializer(steps, many=True).data


  def get_tutorial_likes_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            tutorial_likes = LikeTutorial.objects.filter(owner=user, tutorial=obj).first()
            return tutorial_likes.id if tutorial_likes else None
        return None




  class Meta:
    model = Tutorial
    fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "tutorial_title",
            "tutorial_description",
            "preview_art",
            "tutorial_steps",
             "created_at",
            "updated_at",
            "tutorial_likes_id",
            "tutorial_comments_count",
            "tutorial_likes_count",
    ]