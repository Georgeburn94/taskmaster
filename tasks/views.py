from django.shortcuts import render
from .models import Task, Category

def index(request):
    categories = Category.objects.all()
    tasks = Task.objects.all()
    context = {
        'categories': categories,
        'tasks': tasks,
    }
    return render(request, 'tasks/index.html', context)