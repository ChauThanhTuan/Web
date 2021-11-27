from django.contrib import admin
from polls.models import Blog, Feedback

# Register your models here.
@admin.register(Blog)
class personInfo(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_filter = ('name',)

@admin.register(Feedback)
class feedbackInfo(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message')
    list_filter = ('name', 'email',)
