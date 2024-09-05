from django.db import models
from django.contrib.auth.models import User

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50)  # e.g., 'video', 'quiz', 'flashcards'
    score = models.IntegerField(null=True)  # For quizzes, etc.
    time_spent = models.IntegerField()  # Track time spent on content in seconds
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content_type}"
