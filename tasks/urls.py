from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from .views import TaskViewSet, TaskListViewSet

router = DefaultRouter()
router.register(r'tasklists', TaskListViewSet, basename='tasklist')
tasklists_router = NestedSimpleRouter(router, r'tasklists', lookup='task_list')
tasklists_router.register(r'tasks', TaskViewSet, basename='tasklist-tasks')

tasklists_router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('',include(router.urls)),    #path is empty as adding 'api/' there would double prefix the route (i.e., /api/api)
    path('', include(tasklists_router.urls)),
]
