from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from webapp.models import Task


def index_view(request):
    context = {
        'tasks': Task.objects.all(),
    }
    return render(request, 'index.html', context=context)

def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html')
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        date_completion = request.POST.get('date_completion')

        Task.objects.create(
            description=description,
            status=status,
            date_completion=date_completion if date_completion else None,
        )
        return HttpResponseRedirect('/')


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return HttpResponseRedirect('/')