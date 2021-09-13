from django.contrib import admin
from testapp.models import *
# Register your models here.

class Answerstab(admin.TabularInline):
    model=Answers

class QuestionSet(admin.ModelAdmin):
    inlines=[Answerstab]

admin.site.register(Quiz)
admin.site.register(Questions,QuestionSet)
admin.site.register(Answers)