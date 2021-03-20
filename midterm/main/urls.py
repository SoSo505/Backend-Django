from django.urls import path

from main.views import BookViewSet, JournalViewSet
from rest_framework import routers

router = routers.SimpleRouter()
#router.register('list', TodoListViewSet, basename='main')

urlpatterns = [
    path('books/', BookViewSet.as_view({'get': 'book'})),
    path('journals', JournalViewSet.as_view({'get': 'journal'})),

]

urlpatterns += router.urls