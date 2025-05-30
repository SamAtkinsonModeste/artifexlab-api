from rest_framework import serializers
from .models import Artwork
from likes.models import LikeArtwork


class ArtworkSerializer(serializers.ModelSerializer):
    artwork_owner = serializers.ReadOnlyField(source="owner.username")
    is_artwork_owner = serializers.SerializerMethodField()
    artist_profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    artist_profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    artwork_title = serializers.ReadOnlyField(source="title")
    artwork_description = serializers.ReadOnlyField(source="description")
    artwork_liked_id = serializers.SerializerMethodField()
    artwork_likes_count = serializers.ReadOnlyField()
    # artwork_comments_count = serializers.ReadOnlyField()

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

    def get_is_artwork_owner(self, obj):
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
            "artwork_owner",
            "is_artwork_owner",
            "artist_profile_id",
            "artist_profile_image",
            "created_at",
            "updated_at",
            "artwork_title",
            "artwork_description",
            "image",
              "artwork_liked_id",
            #  "artwork_comments_count",
            "artwork_likes_count",
        ]
