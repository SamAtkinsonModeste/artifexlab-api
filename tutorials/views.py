
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from artlab_api.permissions import IsOwnerOrReadOnly
from .models import Tutorial
from .serializers import TutorialSerializer


class TutorialList(generics.ListCreateAPIView):
    """
    List tutorials or create a tutorial if logged in
    The perform_create method associates the tutorial with the logged in user.
    """

    serializer_class = TutorialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tutorial.objects.annotate(
        tutorial_likes_count=Count("tutorial_likes", distinct=True),
        tutorial_comments_count=Count("tutorial_comments", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        #REVIEW - for related names values in the models
        "owner__followed__owner__profile",
        "tutorial_likes__owner__profile",
        "owner__profile",
    ]

    search_fields = [
        "owner__username",
        "tutorial_title",
    ]

    ordering_fields = [
        #REVIEW - for related name values in the models
        "tutorial_comments_count",
        "tutorial_likes_count",
        "tutorial_likes__created_at",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TutorialDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a tutorial and edit or delete it if you own it.
    """

    serializer_class = TutorialSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Tutorial.objects.annotate(
        #REVIEW - for related names created in the like and comments models
        tutorial_likes_count=Count("tutorial_likes", distinct=True),
        tutorial_comments_count=Count("tutorial_comments", distinct=True),
    ).order_by("-created_at")
