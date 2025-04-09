from django.contrib import admin
from my_app import models
# Register your models here.

admin.site.register(models.Answer)
admin.site.register(models.AnswerLike)
admin.site.register(models.Profile)
admin.site.register(models.Question)
admin.site.register(models.QuestionLike)