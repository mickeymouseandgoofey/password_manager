from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Credential(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=255)
    site_url = models.URLField()
    username = models.CharField(max_length=255)
    password_encrypted = models.TextField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.site_name} ({self.username})"
