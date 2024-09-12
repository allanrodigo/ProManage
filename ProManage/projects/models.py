from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    TODO = 'todo'
    IN_PROGRESS = 'in-progress'
    REVIEW = 'review'
    DONE = 'done'

    STATUS_CHOICES = [
        (TODO, 'to-do'),
        (IN_PROGRESS, 'in-progress'),
        (REVIEW, 'review'),
        (DONE, 'done'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=TODO,
    )
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
