from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

admin.site.register(Status)
admin.site.register(Action)
admin.site.register(TaskComment)

class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'Создать пользователя'
    fk_name = 'user'

class UserAdmin(UserAdmin):
    inlines = (CustomUserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class SpaceAdmin(admin.ModelAdmin):
	list_display = ('name', 'photo', 'status','add_date', 'upd_date','created_by', 'color')
	list_display_links = ('name',)
	search_fields = ('name',)
admin.site.register(Space, SpaceAdmin)

class ListAdmin(admin.ModelAdmin):
	list_display = ('space', 'name_list')
	list_display_links = ('name_list',)
	search_fields = ('name_list',)
admin.site.register(List, ListAdmin)

class TaskAdmin(admin.ModelAdmin):
	list_display = ('task_name', 'dead_line', 'attachments','status','description','start_date','end_date','created_by')
	list_display_links = ('task_name',)
	search_fields = ('name', 'description')
admin.site.register(Task, TaskAdmin)



class SubTaskAdmin(admin.ModelAdmin):
	list_display = ('task_name', 'dead_line', 'attachments','status','description','start_date','end_date','created_by')
	list_display_links = ('task_name',)
	search_fields = ('name', 'description')
admin.site.register(SubTask, SubTaskAdmin)
