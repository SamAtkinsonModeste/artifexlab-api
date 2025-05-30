from rest_framework import serializers
from .models import TutorialSteps


class TutorialStepsSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source="owner.username")
  is_owner = serializers.SerializerMethodField()


  def validate_step_image(self, value):
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


  class Meta:
     model = TutorialSteps
     fields = [
        "id",
        "owner",
        "is_owner",
        "step_number",
        "step_title",
        "step_content",
        "step_image",
        "created_at",
        "updated_at",
     ]