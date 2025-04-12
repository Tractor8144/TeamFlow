from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskListViewSet

router = DefaultRouter()
router.register(r'tasklists', TaskListViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('',include(router.urls)),    #path is empty as adding 'api/' there would double prefix the route (i.e., /api/api)
]
