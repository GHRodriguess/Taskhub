from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.db import IntegrityError
from .models import Task  

# Create your views here.
@login_required
def tasks(request):     
    user = request.user.username
    tasks = Task.objects.filter(user=user, completed=False).order_by('id')    

    if request.method == 'GET':        
        return render(request, 'tasks.html', {'tasks': tasks}) 
    elif request.method == 'POST':
        task = request.POST.get('task')   
        tasks_title = [task.title for task in tasks]
        if task in tasks_title:    
            message = "A tarefa ja existe"
            status = "error"        
            return render(request, 'tasks.html', {'tasks': tasks, "message": message, "status": status}) 
        new_task = Task(title=task, user=user)
        new_task.save()   
        message = "Tarefa adicionada com sucesso"
        status = "success"
        tasks = Task.objects.filter(user=user, completed=False).order_by('id')     
        return render(request, 'tasks.html', {'tasks': tasks, "message": message, "status": status})
    else:
        print("Metodo nao reconheco")
        print(request.method)
        
def logout(request):    
    django_logout(request)
    return redirect('tasks')

def delete(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.delete()
    message = "Tarefa deletada com sucesso"
    status = "success"
    user = request.user.username
    tasks = Task.objects.filter(user=user, completed=False).order_by('id')     
    return render(request, 'tasks.html', {'tasks': tasks, "message": message, "status": status})

def change_status(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.completed = not task.completed
    task.save()
    message = "Status da tarefa atualizado com sucesso"
    status = "success"      
    user = request.user.username  
    tasks = Task.objects.filter(user=user, completed=False).order_by('id')     
    return render(request, 'tasks.html', {'tasks': tasks, "message": message, "status": status})