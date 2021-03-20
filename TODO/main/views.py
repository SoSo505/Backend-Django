# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from auth_.models import MainUser
from main.models import Todotasks,TodoList
from rest_framework.response import Response
from django.shortcuts import render

from main.serializers import TodoListSerializer, TodoTaskSerializer, TodoTaskSerializer2, TodoListSerializer2


class TodotasksSerializer(object):
    pass


class IscompletedTodoListViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def todo_list(self, request):
        todotasks = Todotasks.objects.filter(mark=False)
        serializer = TodotasksSerializer(todotasks, many=True)
        return Response(serializer.data)

    def completed_list(self, request, pk):
        completedtodo = TodoList.objects.get(id=pk)
        completedtodotasks = Todotasks.objects.filter(mark=True)
        serializer = TodotasksSerializer(completedtodotasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id):
        queryset = Todotasks.objects.all()
        todotasks = get_object_or_404(queryset, id=id)
        serializer = TodoTaskSerializer2(todotasks)
        return Response(serializer.data)

    def create(self, request):
        todotasks = Todotasks.objects.create(taskname=request.data.get('task'), created=request.data.get('created'),
                                   due_on=request.data.get('due_on'),
                                   owner=MainUser.objects.get(id=request.data.get('owner')),
                                   mark=request.data.get('mark'),
                                   group=TodoList.objects.get(id=request.data.get('group')))
        todotasks.save()
        serializer = TodoTaskSerializer(todotasks)
        return Response(serializer.data)

    def destroy(self, request, pk):
        todotasks = TodoList.objects.get(pk=pk)
        self.perform_destroy(todotasks)
        return Response(status=status.HTTP_204_NO_CONTENT)






class TodoListViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def todolist(self, request):
        todotasks = TodoList.objects.all()
        serializer = TodoListSerializer(todotasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = TodoList.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TodoListSerializer2(user)
        return Response(serializer.data)

    def create(self, request):
        todoList_data = request.data
        new_todo = TodoList.objects.create(name=request.data.get('name'))
        new_todo.save()
        serializer = TodoListSerializer2(new_todo)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)