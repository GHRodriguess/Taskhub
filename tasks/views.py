from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.db import IntegrityError
from .models import Task  
from .utils import Session

# Create your views here.
@login_required
def tasks(request): 
    session = Session(request)
    user = request.user.username
    tasks = Task.objects.filter(user=user, completed=False).order_by('id')    
    message, status = session.get()
    
    if request.method == 'GET':        
        return render(request, 'tasks.html', {'tasks': tasks, "message": message, "status": status})
    elif request.method == 'POST':
        task = request.POST.get('task')   
        tasks_title = [task.title for task in tasks]
        if task in tasks_title:  
            session.set("A tarefa ja existe", "error")   
            return redirect('tasks')
        new_task = Task(title=task, user=user)
        new_task.save()   
        session.set("Tarefa adicionada com sucesso", "success")         
        return redirect('tasks')
    else:
        print("Metodo nao reconheco", request.method)

@login_required
def logout(request):    
    django_logout(request)
    return redirect('tasks')

@login_required
def delete(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.delete()
    session = Session(request)
    session.set("Tarefa deletada com sucesso", "success")
    return redirect("tasks")

@login_required
def change_status(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.completed = not task.completed
    task.save()
    session = Session(request)
    session.set("Status da tarefa atualizado com sucesso", "success")
    return redirect('tasks')