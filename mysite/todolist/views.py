from asyncio import tasks
from http.client import HTTPResponse
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Task
from django.template import loader
from .forms import TaskForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

 
class IndexClassView(ListView):
    model = Task
    template_name = 'todolist/index.html'
    context_object_name = 'task_list'
class TaskDetail(DetailView):
    model = Task
    template_name = 'todolist/details.html'

# Create your views here.
"""def index(request):
    task_list = Task.objects.all()
    #template = loader.get_template('todolist/index.html')
    context = {
        'task_list': task_list,
    }
    return render(request , 'todolist/index.html' , context)
"""
"""def details(request , tid):
    task = Task.objects.get(pk=tid)
    context = {
        'task':task,
    }
    #return HttpResponse(task.task_desc)
    return render(request , 'todolist/details.html', context)"""
def add(request):
    form = TaskForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('task:index')
    return render(request , 'todolist/task-form.html' , {'form':form})
def taskstatus(request , id):
    task = Task.objects.get(pk=id)
    task.task_status = not task.task_status
    task.save()
    return redirect('task:index')

def edit(request , id):
    task = Task.objects.get(pk=id)
    form = TaskForm(request.POST or None , instance=task)
    if form.is_valid():
        form.save()
        return redirect('task:index')
    return render(request , 'todolist/task-form.html',{'form':form , 'task':task})
def delete(request , id):
    task = Task.objects.get(pk=id)
    if request.method == "POST":
        task.delete()
    
        return redirect('task:index')
    return render(request , 'todolist/delete-task.html' , {'task':task})
