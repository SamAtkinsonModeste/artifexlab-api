from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from artlab_api.permissions import IsOwnerOrReadOnly
from .models import CommentArtwork, CommentTutorial
from .serializers import CommentArtworkSerializer, CommentArtworkDetailSerializer, CommentTutorialSerializer, CommentTutorialDetailSerializer


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
    filterset_fields = ["artwork"]


class CommentTutorialList(BaseCommentList):
    serializer_class = CommentTutorialSerializer
    queryset = CommentTutorial.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tutorial"]


class CommentArtworkDetail(BaseCommentDetail):
    serializer_class = CommentArtworkDetailSerializer
    queryset = CommentArtwork.objects.all()


class CommentTutorialDetail(BaseCommentDetail):
    serializer_class = CommentTutorialDetailSerializer
    queryset = CommentTutorial.objects.all()