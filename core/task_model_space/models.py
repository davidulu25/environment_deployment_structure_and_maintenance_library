from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    PRIORITY_OPTIONS = (
        ("high", "High"),
        ("normal", "Normal"),
        ("low", "Low"),
        )
    
    priority = models.CharField(max_length=6, choices=PRIORITY_OPTIONS)

    TASK_STATUS = (
        ("to-do", "to-do"),
        ("started", "started"),
        ("in progress", "in progress"),
        ("hold", "hold"),
        ("completed", "completed"),
        )
    
    status = models.CharField(max_length=12, choices=TASK_STATUS, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)