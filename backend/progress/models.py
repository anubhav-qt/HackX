from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    disability = models.CharField(max_length=100, blank=True, null=True)

class Progress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    progress_percentage = models.FloatField()
    last_accessed = models.DateTimeField(auto_now=True)
    time_spent = models.FloatField(default=0.0)  # New field to track hours spent

    def __str__(self):
        return f"{self.student.user.username} - {self.content}"