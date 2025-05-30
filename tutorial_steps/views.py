from rest_framework import generics, permissions
from artlab_api.permissions import IsOwnerOrReadOnly
from .models import TutorialSteps
from .serializers import TutorialStepsSerializer


class TutorialStepsList(generics.ListCreateAPIView):
    """
    List of Tutorial steps or create a new step
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TutorialStepsSerializer
    queryset = TutorialSteps.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class TutorialStepsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a tutorial step
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TutorialStepsSerializer
    queryset = TutorialSteps.objects.all()