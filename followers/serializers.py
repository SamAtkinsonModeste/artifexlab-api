from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model.
    The create method handles the unique constraint on 'owner' and 'followed',
    and also prevents a user from following themselves.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    followed_name = serializers.ReadOnlyField(source="followed.username")

    class Meta:
        model = Follower
        fields = ["id", "owner", "created_at", "followed", "followed_name"]


    def validate(self, data):
        request = self.context["request"]
        if data["followed"] == request.user:
            raise serializers.ValidationError("You cannot follow yourself.")
        return data



    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {"detail": "You are already following this user."}
            )
