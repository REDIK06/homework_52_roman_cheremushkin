from django.contrib import admin
from webapp.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date_completion']
    list_filter = ['status']
    search_fields = ['description']