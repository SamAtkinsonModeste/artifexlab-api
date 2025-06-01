from django.contrib import admin
from .models import CommentArtwork, CommentTutorial, CommentTutorialAttempts

# Register your models here.
admin.site.register(CommentArtwork)
admin.site.register(CommentTutorial)
admin.site.register(CommentTutorialAttempts)
