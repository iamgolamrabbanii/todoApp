from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = 'home'),
    path('edit/<int:id>/', home, name='edit_task'),
    path('remove/<int:id>/', remove_task, name = 'remove_task' ),
]
