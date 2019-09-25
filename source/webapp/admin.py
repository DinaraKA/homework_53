from django.contrib import admin
from webapp.models import Task, Status, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'summary', 'description', 'status', 'type', 'created_at']
    list_filter = ['status', 'type']
    list_display_links = ['pk', 'summary', 'description']

admin.site.register(Task, TaskAdmin)
admin.site.register(Status)
admin.site.register(Type)

