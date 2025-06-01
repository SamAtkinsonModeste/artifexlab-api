from django.contrib import admin
from .models import Tutorial, TutorialSteps, TutorialAttempts, TutorialFeedback

# Register your models here.
admin.site.register(Tutorial)
admin.site.register(TutorialSteps)
admin.site.register(TutorialAttempts)
admin.site.register(TutorialFeedback)