from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Rota para login usando a view personalizada
    path('login/', views.custom_login_view, name='login'),
    
    # Rota para logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Rota para cadastro de novo usuário
    path('signup/', views.signup, name='signup'),
    
    # Rota para listagem de projetos (home page após login)
    path('', views.project_list, name='project_list'),
    
    # Rota para detalhes de um projeto específico
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    
    # Rota para criação de um novo projeto
    path('projects/create/', views.project_create, name='project_create'),
    
    # Rota para edição de um projeto existente
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    
    # Rota para exclusão de um projeto existente
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

    path('projects/<int:project_id>/tasks/create/', views.create_task, name='create_task'),

    path('tasks/<int:task_id>/update_status/', views.update_task_status, name='update_task_status'),
    
    path('tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),
]
