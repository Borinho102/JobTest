from django.db import models

# Create your models here.

class Task(models.Model):
    label = models.CharField(verbose_name="Task Label", max_length=256, blank=False)
    created = models.DateTimeField(verbose_name="Created At", auto_now_add=True)
    
    def __str__(self) -> str:
        return self.label
    
