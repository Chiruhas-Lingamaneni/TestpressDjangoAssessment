from django.contrib import admin
from user_app.models import QuestionsList, UserResponse,ResponseList
# Register your models here.

admin.site.register(QuestionsList)
admin.site.register(UserResponse)
admin.site.register(ResponseList)