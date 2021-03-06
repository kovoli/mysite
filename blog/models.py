from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)  # дата будет автоматически добавлена при создании объекта
    update = models.DateTimeField(auto_now=True)  # дата будет автоматически обновляться при сохранении объекта
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


class Meta:
    ordering = ('-publish',)  # сортировать результаты по полю publish


def __str__(self):
    return self.title