from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_todos(request):
    return redirect('todo_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_todos),  # Перенаправление с главной страницы на /todos/
    path('', include('todos.urls')),
]
