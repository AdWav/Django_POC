from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all()
    )

    class Meta:
        model = User
        fields = ['id', 'username',]
