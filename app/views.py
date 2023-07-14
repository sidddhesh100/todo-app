from django.shortcuts import render

# Create your views here.

def to_do_app(request):
    context = dict()
    return render(request, 'todo/home.html', context=context)

def login(request):
    context = dict()
    return render(request, 'todo/login.html', context=context)

def register(request):
    context = dict()
    return render(request, 'todo/register.html', context=context)

def create_task(request):
    context = dict()
    return render(request, 'todo/create-task.html', context=context)