from rest_framework import serializers
from main.models import TodoList, Todotasks


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'

class TodoListSerializer2(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = 'name'

class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todotasks
        fields = '__all__'

class TodoTaskSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Todotasks
        fields = 'taskname, created, owner'