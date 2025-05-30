from rest_framework import serializers
from .models import Artwork
from likes.models import LikeArtwork



class ArtworkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.profile_image.url")
    artwork_liked_id = serializers.SerializerMethodField()
    artwork_likes_count = serializers.ReadOnlyField()
    artwork_comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Validate the image field to ensure it is not too:
        - large (2MB)
        - wide (4096px)
        - tall (4096px)
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError("Image size cannot exceed 2MB!")
        if value.image.width > 4096:
            raise serializers.ValidationError("Image width cannot exceed 4096px!")
        if value.image.height > 4096:
            raise serializers.ValidationError("Image height cannot exceed 4096px!")
        return value

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_artwork_liked_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            artwork_liked = LikeArtwork.objects.filter(owner=user, artwork=obj).first()
            return artwork_liked.id if artwork_liked else None
        return None

    class Meta:
        model = Artwork
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "description",
            "image",
            "artwork_liked_id",
            "artwork_comments_count",
            "artwork_likes_count",
        ]
