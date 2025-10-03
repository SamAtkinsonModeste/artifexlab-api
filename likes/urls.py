from django.urls import path
from likes import views

urlpatterns = [
    path("artwork-likes/", views.LikeArtworkList.as_view()),
    path("artwork-likes/<int:pk>/", views.LikeArtworkDetail.as_view()),
    path("tutorial-likes/", views.LikeTutorialList.as_view()),
    path("tutorial-likes/<int:pk>/", views.LikeTutorialDetail.as_view()),
    path("tutorial-attempt-likes/", views.LikeTutorialAttemptList.as_view()),
    path("tutorial-likes/<int:pk>/", views.LikeTutorialAttemptDetail.as_view()),
]
