from django.shortcuts import render
from app_todo.utility import query

def view(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        result = query("INSERT INTO todo_list (title) VALUES (%s)", [title])
        print(result)

    return render(request, 'app_todo/create.html')