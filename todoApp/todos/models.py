from django.db import models

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=100)
  details = models.CharField(max_length=255)
  isCompleted = models.BooleanField(default=False)


