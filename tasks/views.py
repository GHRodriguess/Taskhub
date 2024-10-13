from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def tasks(request):  
    print(request.user.username)   
    print(request.user.password)   
    return render(request, 'tasks.html')
