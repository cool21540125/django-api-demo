from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):

    # author = models.ForeignKey('auth.User', related_name='author_name')
    title = models.CharField(max_length=20)
    context = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'articles'

