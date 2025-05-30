from rest_framework import generics, permissions
from artlab_api.permissions import IsOwnerOrReadOnly
from likes.models import LikeArtwork, LikeTutorial
from likes.serializers import LikeArtworkSerializer, LikeTutorialSerializer


#NOTE - Created List & Detail BASE views
class BaseLikeList(generics.ListCreateAPIView):
    """
    BaseLike to enable inheritance by all views.
    Attempt at DRY
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class BaseLikeDetail(generics.RetrieveDestroyAPIView):
    """
    BaseLikeDetail to enable inheritance by all views.
    Attempt at DRY
    """
    permission_classes = [IsOwnerOrReadOnly]



#SECTION - Views using the Base Views

class LikeArtworkList(BaseLikeList):
    """
    API view to retrieve a list of artwork likes or create a new artwork like.

    GET: Returns a list of all LikeArtwork instance
    POST: Creates a new artwork_like instance
    """
    serializer_class = LikeArtworkSerializer
    queryset = LikeArtwork.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class LikeArtworkDetail(BaseLikeDetail):
    """
   API view to retrieve, update, or delete a single Artwork instance.

    - GET: Returns the details of the specified Artwork.
    - PUT/PATCH: Updates the specified Artwork.
    - DELETE: Deletes the specified Artwork.
    """
    serializer_class = LikeArtworkSerializer
    queryset = LikeArtwork.objects.all()



class LikeTutorialList(BaseLikeList):
    """
   API view to retrieve a list of tutorial likes or create a new tutorial like.

    GET: Returns a list of all LikeTutorial instance
    POST: Creates a new tutorial_like instance
    """
    serializer_class = LikeTutorialSerializer
    queryset = LikeTutorial.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeTutorialDetail(BaseLikeDetail):
    """
  API view to retrieve, update, or delete a single Tutorial instance.

    - GET: Returns the details of the specified Tutorial.
    - PUT/PATCH: Updates the specified Tutorial.
    - DELETE: Deletes the specified Tutorial.
    """
    serializer_class = LikeTutorial
    queryset = LikeTutorial.objects.all()
