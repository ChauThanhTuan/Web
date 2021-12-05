from django.contrib import admin
from polls.models import Blog, Feedback

# Register your models here.
@admin.register(Blog)
class personInfo(admin.ModelAdmin):
    list_display = ('id', 'topic', 'title', 'description','images', 'link')
    list_filter = ('topic',)

@admin.register(Feedback)
class feedbackInfo(admin.ModelAdmin):
    list_display = ('id',  'time', 'name', 'email', 'subject', 'message')
    list_filter = ('name', 'email', 'time')
