from django.urls import path
from comments import views

urlpatterns = [
    path("artwork-comments/", views.CommentArtworkList.as_view()),
    path("artwork-comments/<int:pk>/", views.CommentArtworkDetail.as_view()),
    path("tutorial-comments/", views.CommentTutorialList.as_view()),
    path("tutorial-comments/<int:pk>/", views.CommentTutorialDetail.as_view()),
]
