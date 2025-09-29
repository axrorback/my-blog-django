from django.db import models

# Create your models here.
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True, help_text="GitHub yoki demo link")
    image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
