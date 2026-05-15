from django.db import models
# Create your models here.
class MyCategory(models.Model):
    category_name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.category_name