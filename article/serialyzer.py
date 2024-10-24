from rest_framework import serializers
from .models import Article

class ArticleSerialyzer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'article',
            'owner',
            'created',
        ]

