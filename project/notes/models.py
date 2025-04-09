from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', null=True)



    def __str__(self):
        return self.title
