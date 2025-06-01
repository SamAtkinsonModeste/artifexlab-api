
from django.db.models import Count
from rest_framework import generics, permissions, filters
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from artlab_api.permissions import IsOwnerOrReadOnly
from .models import Tutorial, TutorialSteps, TutorialAttempts, TutorialFeedback
from .serializers import TutorialSerializer, TutorialStepsSerializer, TutorialAttemptsSerializer, TutorialFeedbackSerializer

class BaseTutorialList(generics.ListCreateAPIView):
    """
    Base view for ListCreateAPIView with:
    - IsAuthenticatedOrReadOnly permissions
    - Auto-assignment of request user as owner on creation
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




class TutorialsList(BaseTutorialList):
    """
    List tutorials or create a tutorial if logged in
    """

    serializer_class = TutorialSerializer
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

class TutorialStepsList(BaseTutorialList):
    """
    List all tutorial steps or create a new step.
    Used for backend access and tutorial step management.
    """
    serializer_class = TutorialStepsSerializer
    queryset =TutorialSteps.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tutorial"]


class TutorialAttemptsList(BaseTutorialList):
    """
     List all tutorial attempts or create a new attempt submission.
     All logged-in users can contribute attempts.
    """
    serializer_class = TutorialAttemptsSerializer
    queryset =TutorialAttempts.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tutorial_tried"]


class TutorialFeedbackList(BaseTutorialList):
    """
    List all tutorial feedback
    or create new feedback - if the tutorial authenticated
    is the tutorial owner of the attempt.
    Feedback is intended to be mentor guidance on a user's attempt.
    """
    serializer_class = TutorialFeedbackSerializer
    queryset =TutorialFeedback.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tutorial_attempt"]


class BaseTutorialDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Base detail view for retrieving, updating,
    or deleting objects with IsOwnerOrReadOnly permissions.
    """
    permission_classes = [IsOwnerOrReadOnly]




class TutorialDetail(BaseTutorialDetail):
    """
   API view to retrieve, update, or delete a single Tutorial.

    - GET: Returns the details of the specified Tutorial.
    - PUT/PATCH: Updates the specified Tutorial.
    - DELETE: Deletes the specified Tutorial.
    """
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.annotate(
        #REVIEW - for related names created in the like and comments models
        tutorial_likes_count=Count("tutorial_likes", distinct=True),
        tutorial_comments_count=Count("tutorial_comments", distinct=True),
    ).order_by("-created_at")


class TutorialStepDetail(BaseTutorialDetail):
    """
  API view to retrieve, update, or delete a single Tutorial Step.

    - GET: Returns the details of the specified Tutorial step.
    - PUT/PATCH: Updates the specified Tutorial step.
    - DELETE: Deletes the specified Tutorial step.
    """
    serializer_class = TutorialStepsSerializer
    queryset = TutorialSteps.objects.all()

class TutorialAttemptDetail(BaseTutorialDetail):
    """
  API view to retrieve, update, or delete a single Tutorial Attempt.

  - GET: Returns the details of the specified Tutorial Attempt.
  - PUT/PATCH: Updates the specified Tutorial Attempt.
  - DELETE: Deletes the specified Tutorial Attempt.
    """
    serializer_class = TutorialAttemptsSerializer
    queryset = TutorialAttempts.objects.all()

class TutorialFeedbackDetail(BaseTutorialDetail):
    """
  API view to retrieve, update, or delete a single Tutorial Feedback.

    - GET: Returns the details of the specified Tutorial Feedback.
    - PUT/PATCH: Updates the specified Tutorial Feedback.
    - DELETE: Deletes the specified Tutorial Feedback.
    """
    serializer_class = TutorialFeedbackSerializer
    queryset = TutorialFeedback.objects.all()

    def perform_create(self, serializer):
        tutorial_attempt = serializer.validated_data.get("feedback_entries")
        tutorial_owner = tutorial_attempt.tutorial_tried.owner

        if self.request.user != tutorial_owner:
            raise PermissionDenied("Only the tutorial owner can give feedback.")

        serializer.save(owner=self.request.user)
