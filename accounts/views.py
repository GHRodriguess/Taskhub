from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.http.response import HttpResponse
from django.db.models import Q 
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login_django(request, user)
            return redirect('tasks')
        else:
            message = "Nome de usuário ou senha estão incorretos"
            return render(request, "login.html", {"message": message, "username": username, "password": password, "class": "error"})
        return render(request, "login.html")
    else:
        print("Metodo nao reconheco")
        print(request.method)
    
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')  
        user = User.objects.filter(Q(username=username) | Q(email=email)).first()           
        if user:
            message = ""
            if user.username == username:
                message = "Esse nome de usuário já existe"
                return render(request, "register.html", {"message": message, "username": username, "email": email, "password": password, "class": "error"})
            elif user.email == email:
                message = "Email já cadastrado"
                return render(request, "register.html", {"message": message, "username": username, "email": email, "password": password, "class": "error"})
        else:            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            message = "Usuário cadastrado com sucesso"
            return render(request, "login.html", {"message": message, "username": username,"class": "sucess"})
    else:
        print("Metodo nao reconheco")
        print(request.method)