from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from artlab_api.permissions import IsOwnerOrReadOnly
from .models import CommentArtwork, CommentTutorial, CommentTutorialAttempts
from .serializers import CommentArtworkSerializer, CommentArtworkDetailSerializer, CommentTutorialSerializer, CommentTutorialDetailSerializer, CommentTutorialAttemptSerializer, CommentTutorialAttemptDetailSerializer


class BaseCommentList(generics.ListCreateAPIView):
    """
    BaseCommentList to enable inheritance by all list views.
    DRY
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BaseCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    BaseCommentDetail to enable inheritance by all views.
    DRY
    """
    permission_classes = [IsOwnerOrReadOnly]

class CommentArtworkList(BaseCommentList):
    serializer_class = CommentArtworkSerializer
    queryset = CommentArtwork.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["artwork", "owner"]


class CommentTutorialList(BaseCommentList):
    serializer_class = CommentTutorialSerializer
    queryset = CommentTutorial.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tutorial", "owner"]

class CommentTutorialAttemptList(BaseCommentList):
    serializer_class = CommentTutorialAttemptSerializer
    queryset = CommentTutorialAttempts.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tutorial_attempts", "owner"]


class CommentArtworkDetail(BaseCommentDetail):
    serializer_class = CommentArtworkDetailSerializer
    queryset = CommentArtwork.objects.all()


class CommentTutorialDetail(BaseCommentDetail):
    serializer_class = CommentTutorialDetailSerializer
    queryset = CommentTutorial.objects.all()

class CommentTutorialAttemptDetail(BaseCommentDetail):
    serializer_class = CommentTutorialAttemptDetailSerializer
    queryset = CommentTutorialAttempts.objects.all()