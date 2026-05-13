from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Task.objects.create(title=title)

        return redirect('/')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()

    return redirect('/')
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.completed = 'completed' in request.POST
        task.save()

        return redirect('/')

    return render(request, 'tasks/update_task.html', {'task': task})
