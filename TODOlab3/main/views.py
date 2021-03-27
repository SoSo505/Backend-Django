
from django.shortcuts import render

# Create your views here.


def todo_list(request):
    todotasks = [{
        'task': 'Task 1',
        'created': '12/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': False,
    },{
        'task': 'Task 2',
        'created': '12/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': False,
    },{
        'task': 'Task 3',
        'created': '12/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': False,
    },{
        'task': 'Task 4',
        'created': '12/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': False,
    }]

    return render(request, 'todo_list.html', {"todotasks": todotasks})


def completed_list(request, pk):
    completedtodotasks = [{
        'task': 'Task 0',
        'created': '12/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': True,
    }]

    return render(request, 'completed_todo_list.html', {"completedtodotasks":completedtodotasks, 'id':pk})

