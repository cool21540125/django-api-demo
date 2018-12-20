from django.db import models

class Article(models.Model):

    author = models.ForeignKey('User', related_name='author_name')
    title = models.CharField(max_length=20)
    context = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title


class User(models.Model):

    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name
