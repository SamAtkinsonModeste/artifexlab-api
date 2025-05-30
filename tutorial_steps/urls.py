from django.urls import path
from tutorial_steps import views

urlpatterns = [
    path("tutorial-steps/", views.TutorialStepsList.as_view()),
    path("tutorial-steps/<int:pk>/", views.TutorialStepsDetail.as_view()),
]