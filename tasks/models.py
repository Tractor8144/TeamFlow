from django.db import models
from django.conf import settings

# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=255)
    # created_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name='taskslist'
    # )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name