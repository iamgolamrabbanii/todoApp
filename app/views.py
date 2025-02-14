from django.shortcuts import render, redirect
from .models import database
from datetime import datetime, timedelta
def home(request, id = None):
    task = None
    if id : 
        task = database.objects.get(id = id)
    if request.method == "POST":
        tit = request.POST.get('title')
        des = request.POST.get('description')
        time = request.POST.get('endtime')
        if task :
            task.task_title = tit
            task.task_description = des
            task.endtime = time
            task.save()
        elif des and tit:
            database.objects.create(task_title = tit, task_description = des, endtime = time)
        return redirect('/')
    context = {
        'editTask': task, 
        'tasks':database.objects.all(),
        'current_time' : (datetime.now() + timedelta(hours=1)).strftime('%H') + ":00"
    }
    return render(request, 'index.html', context)


def remove_task(request, id) :
    task = database.objects.get(id = id)
    task.delete()

    return redirect('/')