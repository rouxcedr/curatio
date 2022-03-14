from django.contrib import admin
from .models import *

admin.site.register(TrainingCourse)
admin.site.register(Video)
admin.site.register(TrainingVideo)
admin.site.register(VideoQuizz)
admin.site.register(QuizzQuestion)
admin.site.register(QuestionPossibleAnswer)
admin.site.register(ProgressionTracking)