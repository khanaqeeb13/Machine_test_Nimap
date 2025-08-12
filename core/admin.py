from django.contrib import admin
from .models import Client, Project

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'created_by', 'created_at')
    search_fields = ('client_name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'client', 'created_by', 'created_at')
    list_filter = ('client',)
    search_fields = ('project_name',)
