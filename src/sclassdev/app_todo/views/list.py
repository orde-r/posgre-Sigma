from django.shortcuts import render
from app_todo.utility import query

def view(request):
    if request.method == "GET":
        posts = query("SELECT * FROM todo_list ORDER BY ID DESC") 
    return render(request, 'app_todo/list.html', {'posts' : posts})
