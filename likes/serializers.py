from django.db import IntegrityError
from rest_framework import serializers
from .models import LikeArtwork, LikeTutorial


class LikeBaseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    Adds three extra fields when returning a list of Like instances
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        fields = ["id", "owner", "created_at"]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {"detail": "You have already liked this!"}
            )

class LikeArtworkSerializer(LikeBaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = LikeArtwork
        fields = LikeBaseSerializer.Meta.fields + ["artwork"]



class LikeTutorialSerializer(LikeBaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = LikeTutorial
        fields = LikeBaseSerializer.Meta.fields + ["tutorial"]