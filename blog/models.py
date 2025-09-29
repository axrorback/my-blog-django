from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)  # avtomatik yaratiladi
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # slug avtomatik generatsiya bo‘lishi uchun
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
