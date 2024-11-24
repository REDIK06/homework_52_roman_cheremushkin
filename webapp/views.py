from django.shortcuts import render
from webapp.models import Task


def index_view(request):
    context = {
        'tasks': Task.objects.all(),
    }
    return render(request, 'index.html', context=context)