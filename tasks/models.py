from django.db import models
from categorys.models import MyCategory
# Create your models here.
class MyTask(models.Model):
    task_title = models.CharField(max_length=20)
    task_description = models.TextField(max_length=200)
    is_complete = models.BooleanField(default=False)
    task_assign_date = models.DateField()
    task_category = models.ManyToManyField(MyCategory)

    def __str__(self):
        return self.task_title