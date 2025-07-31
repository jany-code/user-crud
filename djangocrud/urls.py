"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from session import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='task'),
    path('tasks/completed_list', views.tasks_completed_list, name='tasks_completed_list'),
    path('task_details/<int:task_id>', views.task_detail, name='task_detail'),
    path('task_completed/<int:task_id>', views.task_completed, name='task_completed'),
    path('task_delete/<int:task_id>', views.task_delete, name='task_delete'),
    path('logout/', views.cerrar_session, name='logout'),
    path('login/', views.iniciar_sesion, name='login'),
    path('New-task/', views.create_task, name='create_task'),
    path('health/', views.healthcheck),
]
