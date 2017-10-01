from django.db import models

class blogArticle(models.Model):
    class Meta():
        verbose_name_plural = 'Статьи'
    title = models.CharField(default="", max_length=255, verbose_name='Название статьи')
    text = models.TextField(default="", max_length=1300, verbose_name='Текст')
