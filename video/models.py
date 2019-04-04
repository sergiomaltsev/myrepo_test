from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
#hello


class Video(models.Model):
    class Meta():
        db_table='Video'
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео_много'

    url = models.URLField()
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    dis = models.TextField(blank=True, null=True)
    like = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta():
        db_table='Comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    like = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text[:20]
# Create your models here.
