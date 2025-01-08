from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category

def index(request):
    categories = Category.objects.all()
    tasks = Task.objects.all()
    context = {
        'categories': categories,
        'tasks': tasks,
    }
    return render(request, 'tasks/index.html', context)

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    # Add your edit logic here
    return redirect('tasks:index')

def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = True
    task.save()
    return redirect('tasks:index')

def incomplete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = False
    task.save()
    return redirect('tasks:index')

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('tasks:index')