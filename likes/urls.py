from django.urls import path
from likes import views

urlpatterns = [
    path("likesArtwork/", views.LikeArtworkList.as_view()),
    path("likesArtwork/<int:pk>/", views.LikeArtworkDetail.as_view()),

]
