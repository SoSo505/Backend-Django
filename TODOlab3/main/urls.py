from django.urls import path

from main.views import todo_list, completed_list

urlpatterns = [
    path('todos/', todo_list),
    path('todos/<int:pk>/completed', completed_list)
]