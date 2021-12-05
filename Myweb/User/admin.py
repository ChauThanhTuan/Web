from django.contrib import admin

from User.models import User

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'country', 'birthday')
    list_search = ('name')
    list_filter = ('gender', 'country')
