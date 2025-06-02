from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    profile_image = serializers.ReadOnlyField(source="profile.profile_image.url")
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    artworks_count = serializers.ReadOnlyField()
    tutorials_count = serializers.ReadOnlyField()
    tutorials_attempt_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            print(following)
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "display_name",
            "bio",
            "profile_image",
            "is_owner",
            "following_id",
            "artworks_count",
            "tutorials_count",
            "tutorials_attempt_count",
            "followers_count",
            "following_count",
        ]
