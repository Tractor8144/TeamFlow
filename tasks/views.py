from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, TaskList
from .serializers import TaskSerializer, TaskListSerializer
# Create your views here.

class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
