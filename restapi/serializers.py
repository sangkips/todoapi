from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'todos']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'task']

