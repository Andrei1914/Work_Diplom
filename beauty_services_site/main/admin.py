from django.contrib import admin
from .models import *


admin.site.register(Category)


@admin.register(WorkExample)
class WorkExampleAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('title', 'category', 'date_publish')
    list_filter = ('date_publish', 'category')
    search_fields = ('category', 'date_publish')



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_per_page = 24
    list_display = ('user', 'content', 'date_publish')
    list_filter = ('date_publish', 'user')
    search_fields = ('user', 'date_publish')


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ('user_id', 'name', 'phone_number', 'password', 'is_verified')
    list_filter = ('is_verified', 'name')
    search_fields = ('name', 'is_verified')



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ('user_id', 'service', 'date_service')
    list_filter = ('date_service', 'user_id')
    search_fields = ('user_id', 'date_service')



@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('user_id', 'message', 'date_publish')
    list_filter = ('date_publish', 'user_id')
    search_fields = ('user_id', 'date_publish')