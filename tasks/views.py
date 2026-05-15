from django.shortcuts import render,redirect
from . import forms 
from . import models 
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_item = forms.TaskForm(request.POST)
        if task_item.is_valid():
            task_item.save()
            return redirect('add_task')
    else:
        task_item = forms.TaskForm()
    return render(request,'task.html',{'form': task_item})

def edit_task(request,id):
    task = models.MyTask.objects.get(pk=id)
    task_item = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_item = forms.TaskForm(request.POST,instance=task)
        if task_item.is_valid():
            task_item.save()
            return redirect('add_task')
    # else:
    #     task_item = forms.TaskForm()
    return render(request,'task.html',{'form' : task_item})

def delete_task(request,id):
    task = models.MyTask.objects.get(pk=id)
    task.delete()
    return redirect('show_page')