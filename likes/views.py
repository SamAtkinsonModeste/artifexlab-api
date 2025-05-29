from rest_framework import generics, permissions
from artlab_api.permissions import IsOwnerOrReadOnly
from likes.models import LikeArtwork, LikeTutorial
from likes.serializers import LikeArtworkSerializer, LikeTutorialSerializer

class BaseLikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BaseLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]


class LikeArtworkList(BaseLikeList):
    serializer_class = LikeArtworkSerializer
    queryset = LikeArtwork.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeArtworkDetail(BaseLikeDetail):
    """
    Retrieve a like or delete it by id if you own it.
    """
    serializer_class = LikeArtworkSerializer
    queryset = LikeArtwork.objects.all()

# class LikeList(generics.ListCreateAPIView):
#     """
#     List likes or create a like if logged in.
#     """

#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     serializer_class = LikeSerializer
#     queryset = Like.objects.all()

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class LikeDetail(generics.RetrieveDestroyAPIView):
#     """
#     Retrieve a like or delete it by id if you own it.
#     """

#     permission_classes = [IsOwnerOrReadOnly]
#     serializer_class = LikeSerializer
#     queryset = Like.objects.all()
