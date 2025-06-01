from django.contrib import admin
from .models import LikeArtwork, LikeTutorial, LikeTutorialAttempt

#Register your models here.
admin.site.register(LikeArtwork)
admin.site.register(LikeTutorial)
admin.site.register(LikeTutorialAttempt)
