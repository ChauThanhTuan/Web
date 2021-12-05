from django.contrib import admin
from polls.models import Blog

class credentialUser(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_filter = ('name',)

from django.contrib import admin

class credentialUser(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_filter = ('name',)
