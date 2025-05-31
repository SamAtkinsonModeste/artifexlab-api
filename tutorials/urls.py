from django.urls import path
from tutorials import views

urlpatterns = [
    path("tutorials/", views.TutorialsList.as_view()),
    path("tutorials/<int:pk>/", views.TutorialDetail.as_view()),
    path("tutorial-steps/", views.TutorialStepsList.as_view()),
    path("tutorial-steps/<int:pk>/", views.TutorialStepDetail.as_view()),
    path("tutorial-attempts/", views.TutorialAttemptsList.as_view()),
    path("tutorial-attempts/<int:pk>/", views.TutorialAttemptDetail.as_view()),
    path("tutorial-feedbacks/", views.TutorialFeedbackList.as_view()),
    path("tutorial-feedbacks/<int:pk>/", views.TutorialFeedbackDetail.as_view()),
]
