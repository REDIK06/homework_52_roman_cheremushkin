from django.urls import path
from webapp.views import index_view, task_create_view, task_delete

urlpatterns = [
    path('', index_view),
    path('create/', task_create_view),
    path('delete/<int:pk>/', task_delete, name='task_delete'),
]