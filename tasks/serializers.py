from rest_framework import serializers
from .models import Task, TaskList

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ['id', 'name', 'description']

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_by', 'assigned_to', 'task_list']