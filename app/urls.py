from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('remvoe/<int:id>', remove_task, name = "remove_task" )
]
