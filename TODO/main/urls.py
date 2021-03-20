from django.urls import path

from main.views import IscompletedTodoListViewSet, TodoListViewSet
from rest_framework import routers

router = routers.SimpleRouter()
#router.register('list', TodoListViewSet, basename='main')

urlpatterns = [
    path('todos/', TodoListViewSet.as_view({'get': 'todo_list', 'post': 'create'})),
    path('todos/<int:pk>', IscompletedTodoListViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('todos/<int:pk>/completed', IscompletedTodoListViewSet.as_view({'get': 'completed_todo_list'})),
]

urlpatterns += router.urls