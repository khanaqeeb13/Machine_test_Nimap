from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Client, Project

User = get_user_model()

class UserBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username'] 

class ProjectBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    projects = ProjectBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at', 'projects']

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.client_name', read_only=True)
    users = UserBriefSerializer(many=True, read_only=True)
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

class ClientWithUserProjectsSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    projects = ProjectBriefSerializer(many=True, read_only=True)
    user_projects = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = [
            'id', 'client_name', 'created_at', 'created_by', 'updated_at',
            'projects', 'user_projects'
        ]

    def get_user_projects(self, obj):
        # Get all unique projects assigned to users in this client's projects
        user_projects = Project.objects.filter(users__in=obj.projects.values_list('users', flat=True)).distinct()
        return ProjectBriefSerializer(user_projects, many=True).data

class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_name', 'users']

        