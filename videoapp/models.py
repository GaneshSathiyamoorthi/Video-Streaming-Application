
from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField() # Consider changing this to FileField if you want to store videos locally
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Add more fields such as tags, category, etc. based on your requirements
    
    def __str__(self):
        return self.name

