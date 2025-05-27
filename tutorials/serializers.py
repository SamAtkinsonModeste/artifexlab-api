from rest_framework import serializers
from .models import Tutorial
from likes.models import Like

class TutorialSerializer(serializers.ModelSerializer):
  tutorial_owner = serializers.ReadOnlyField(source="owner.username")
  is_tutorial_owner = serializers.SerializerMethodField()
  tutor_profile_id = serializers.ReadOnlyField(source="owner.profile.id")
  tutor_profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
  tutorial_liked_id = serializers.SerializerMethodField()
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





  def get_is_tutorial_owner  (self, obj):
    request = self.context["request"]
    return request.user == obj.owner


  def get_tutorial_liked_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            tutorial_liked = Like.objects.filter(owner=user, tutorial=obj).first()
            return tutorial_liked.id if tutorial_liked else None
        return None




  class Meta:
    model = Tutorial
    fields = [
       "id",
            "tutorial_owner",
            "is_tutorial_owner",
            "tutor_profile_id",
            "tutor_profile_image",
            "created_at",
            "updated_at",
            "tutorial_title",
            "tutorial_description",
            "preview_art",
            "tutorial_liked_id",
            "tutorial_comments_count",
            "tutorial_likes_count",
    ]