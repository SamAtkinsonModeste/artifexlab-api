from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import CommentArtwork, CommentTutorial, CommentTutorialAttempts


class BaseCommentSerializer(serializers.ModelSerializer):
    """
       This serializer provides shared fields and logic for displaying comment instances,
    including owner details, profile image, and human-readable timestamps.
    It is intended to be extended by app-specific comment serializers (e.g., ArtworkCommentSerializer, TutorialCommentSerializer).

    Fields added:
    - owner: Username of the comment's owner.
    - is_owner: Boolean indicating if the requesting user is the comment owner.
    - profile_id: ID of the owner's profile.
    - profile_image: URL of the owner's profile image.
    - created_at: Human-readable creation time (e.g., '3 minutes ago').
    - updated_at: Human-readable update time.

    The 'content' field is expected to be defined in the subclass's Meta model.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ImageField(source="owner.profile.profile_image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "content",
        ]


class CommentArtworkSerializer(BaseCommentSerializer):
    """
    Serializer for creating and listing comments on artworks.
     Inherits shared fields and logic from BaseCommentSerializer and adds the 'artwork' field to associate the comment with a specific artwork.

    """

    class Meta:
        model = CommentArtwork
        fields = BaseCommentSerializer.Meta.fields + ["artwork"]


class CommentArtworkDetailSerializer(CommentArtworkSerializer):
    """
    Serializer for the CommentArtwork model used in Detail view
    artwork is a read only field so that we don't have to set it on each update
    """

    artwork = serializers.ReadOnlyField(source="artwork.id")


class CommentTutorialSerializer(BaseCommentSerializer):
    """
    Serializer for creating and listing comments on tutorials.
    Inherits shared fields and logic from BaseCommentSerializer and adds the 'tutorial' field to associate the comment with a specific tutorial.

    """

    class Meta:
        model = CommentTutorial
        fields = BaseCommentSerializer.Meta.fields + ["tutorial"]


class CommentTutorialDetailSerializer(CommentTutorialSerializer):
    """
    Serializer for the CommentTutorial model used in Detail view
    tutorial is a read only field so that we don't have to set it on each update
    """

    tutorial = serializers.ReadOnlyField(source="tutorial.id")


class CommentTutorialAttemptSerializer(BaseCommentSerializer):
    """
    Serializer for creating and listing comments on tutorials.
    Inherits shared fields and logic from BaseCommentSerializer and adds the 'tutorial_attempts' field to associate the comment with a specific tutorial.

    """

    class Meta:
        model = CommentTutorialAttempts
        fields = BaseCommentSerializer.Meta.fields + ["tutorial_attempts"]


class CommentTutorialAttemptDetailSerializer(CommentTutorialAttemptSerializer):
    """
    Serializer for the CommentTutorialAttpts model used in Detail view
    tutorial_attempts is a read only field so that we don't have to set it on each update
    """

    tutorial_attempts = serializers.ReadOnlyField(source="tutorial_attempts.id")
