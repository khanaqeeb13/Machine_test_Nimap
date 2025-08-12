from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer, ClientWithUserProjectsSerializer, ProjectCreateSerializer
from django.contrib.auth import get_user_model
from django.http import Http404

User = get_user_model()

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('-created_at')
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save()
    
    # If we want to do not want to enter the data from api we can comment the data
    def get_serializer_class(self):
        if self.action == 'add_project':
            return ProjectCreateSerializer
        return ClientSerializer

    @action(detail=True, methods=['post'], url_path='projects')
    def add_project(self, request, pk=None):
        client = self.get_object()
        serializer = ProjectCreateSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save(client=client, created_by=request.user)
            return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = ClientWithUserProjectsSerializer(instance)
        return Response(serializer.data)

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.all()
    

