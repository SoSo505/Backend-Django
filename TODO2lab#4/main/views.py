# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from main.models import Todotasks, Todocompleteornot

from django.shortcuts import render

# Create your views here.
def todo_list(request):
    todotasks = Todotasks.objects.filter(mark=False)
    return render(request, 'todo_list.html', {"todotasks": todotasks})

def completed_list(request, pk):
    completedtodo = Todocompleteornot.objects.get(id=pk)
    completedtodotasks = Todotasks.objects.filter(mark=True)
    return render(request, 'completed_todo_list.html', {"completedtodotasks": completedtodotasks, 'id': pk})