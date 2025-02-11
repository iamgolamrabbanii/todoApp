from django.shortcuts import render, redirect
from .models import database
from datetime import datetime, timedelta
def home(request):
    if request.method == "POST":
        tit = request.POST.get('title')
        des = request.POST.get('description')
        time = request.POST.get('endtime')
        if des :
            database.objects.create(task_title = tit, task_description = des, endtime = time)
        redirect('/')
    context = {
        'tasks':database.objects.all(),
        'current_time' : (datetime.now() + timedelta(hours=1)).strftime('%H') + ":00"
    }
    return render(request, 'index.html', context)
def remove_task(request, id) :
    task = database.objects.get(id = id)
    task.delete()

    return redirect('/')