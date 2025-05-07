# TaskHub - Task Manager


TaskHub é uma aplicação web desenvolvida com Django que permite aos usuários gerenciar seus afazeres diários. Com ela, você pode adicionar, visualizar, editar e excluir suas tarefas de forma simples e organizada.

## Funcionalidades
* Adicionar tarefas: Crie novas tarefas para organizar seu dia a dia.
* Editar tarefas: Atualize as tarefas conforme o progresso ou mudanças nas prioridades.
* Excluir tarefas: Remova as tarefas concluídas ou que não são mais relevantes.
* Visualizar tarefas: Veja todas as suas tarefas ativas em uma lista fácil de navegar.
* Autenticação de usuário: Registre-se e faça login para acessar suas tarefas pessoais.
* Interface intuitiva: Interface simples e amigável para facilitar o gerenciamento dos afazeres.

## Tecnologias Utilizadas
* Python: Linguagem principal usada no back-end.
* Django: Framework web utilizado para construir a aplicação.
* HTML/CSS: Para a construção da interface web.
* SQLite: Banco de dados padrão para armazenamento de tarefas.
 
## Instalação e Configuração
### Para rodar localmente na sua máquina você precisa de:
* Python >= 3.10
* Executar os seguintes comandos:
* Para Windows
~~~windows:
python -m venv venv
venv\Scripts\activate
git clone https://github.com/GHRodrigues/Taskhub.git
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
~~~
* Para Linux/Mac
~~~linux/mac:
python3 -m venv venv
source venv/bin/activate
git clone https://github.com/GHRodrigues/Taskhub.git
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
~~~
* E acessar a aplicação no seu navegador:
[http://localhost:8000/](http://localhost:8000/)


### Acessando o site
* Agora para acessar o projeto diretamente em um site, acesse:
[https://ghrodriguess.pythonanywhere.com](https://ghrodriguess.pythonanywhere.com).

 

