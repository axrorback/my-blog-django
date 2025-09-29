from django.db import models

# Create your models here.
from django.db import models


class About(models.Model):
    title = models.CharField(max_length=150, default="About Me")
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
