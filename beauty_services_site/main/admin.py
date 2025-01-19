from django.contrib import admin
from .models import *


admin.site.register(Category)


@admin.register(WorkExample)
class WorkExampleAdmin(admin.ModelAdmin):
    list_per_page = 30 #максимально число записей
    list_display = ('title', 'category', 'date_publish') #что будет отображаться на странице admin
    list_filter = ('date_publish', 'category') #фильтры для отображаемых полей
    search_fields = ('category', 'date_publish') #поиск в полях по введенным данным



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_per_page = 24 #максимально число записей
    list_display = ('user', 'content', 'date_publish') #что будет отображаться на странице admin
    list_filter = ('date_publish', 'user') #фильтры для отображаемых полей
    search_fields = ('user', 'date_publish') #поиск в полях по введенным данным


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_per_page = 100 #максимально число записей
    list_display = ('user_id', 'name', 'phone_number', 'password', 'is_verified') #что будет отображаться на странице admin
    list_filter = ('is_verified', 'name') #фильтры для отображаемых полей
    search_fields = ('name', 'is_verified') #поиск в полях по введенным данным



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 100 #максимально число записей
    list_display = ('user_id', 'service', 'date_service') #что будет отображаться на странице admin
    list_filter = ('date_service', 'user_id') #фильтры для отображаемых полей
    search_fields = ('user_id', 'date_service') #поиск в полях по введенным данным



@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    list_per_page = 50 #максимально число записей
    list_display = ('user_id', 'message', 'date_publish')  #что будет отображаться на странице admin
    list_filter = ('date_publish', 'user_id') #фильтры для отображаемых полей
    search_fields = ('user_id', 'date_publish') #поиск в полях по введенным данным