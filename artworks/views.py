from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from artlab_api.permissions import IsOwnerOrReadOnly
from .models import Artwork
from .serializers import ArtworkSerializer


class ArtworkList(generics.ListCreateAPIView):
    """
    List artworks or create a new artwork if logged in.
    The perform_create method associates the artwork with the logged-in user.
    """

    serializer_class = ArtworkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Artwork.objects.annotate(
        artworks_likes_count=Count("artwork_likes", distinct=True),
        # comments_count=Count("comments", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        "owner__followed__owner__profile",
        "artwork_likes__owner__profile",
        "owner__profile",
    ]

    search_fields = [
        "owner__username",
        "title",
    ]

    ordering_fields = [
        #  "comments_count",
        "artwork_likes_count",
        "artwork_likes__created_at",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArtworkDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an artwork and edit or delete it if you own it.
    """

    serializer_class = ArtworkSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Artwork.objects.annotate(
        artwork_likes_count=Count("artwork_likes", distinct=True),
        # comments_count=Count("comments", distinct=True),
    ).order_by("-created_at")