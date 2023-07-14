from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.to_do_app, name="home"),
    path('login/', view=views.login, name="login"),
    path('register/', view=views.register, name="register"),
    path('create_task/', view=views.create_task, name="createTask"),
]
