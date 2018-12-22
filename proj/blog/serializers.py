from rest_framework import serializers
from .models import User, Article

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('author', 'title', 'context')

