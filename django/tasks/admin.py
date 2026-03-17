from django.contrib import admin
from tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at')

    list_filter = ('completed',)

    search_fields = ('title',)

admin.site.register(Task, TaskAdmin)