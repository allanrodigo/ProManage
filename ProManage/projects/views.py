from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm, ProjectForm, TaskForm, TaskFormSet
from django.contrib.auth import views as auth_views
from .models import Project, Task

import logging
import json

logger = logging.getLogger(__name__)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('project_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def project_list(request):
    logger.debug("Entrando na view project_list. Usuário autenticado: %s', request.user.username")
    projects = Project.objects.filter(owner=request.user)
    
    if projects:
        logger.debug('Projetos carregados para o usuário: %s', request.user.username)
    else:
        logger.debug('Nenhum projeto encontrado para o usuário: %s', request.user.username)

    return render(request, 'projects/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)

    tasks_todo = project.task_set.filter(status=Task.TODO)
    tasks_in_progress = project.task_set.filter(status=Task.IN_PROGRESS)
    tasks_review = project.task_set.filter(status=Task.REVIEW)
    tasks_done = project.task_set.filter(status=Task.DONE)

    form = TaskForm()

    columns = [
        ('to-do', tasks_todo),
        ('in-progress', tasks_in_progress),
        ('review', tasks_review),
        ('done', tasks_done),
    ]

    return render(request, 'projects/project_detail.html', {
        'project': project,
        'columns': columns,
        'form': form,
    })

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'projects/project_create.html', {'form': form})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        formset = TaskFormSet(request.POST, instance=project)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
        formset = TaskFormSet(instance=project)
    return render(request, 'projects/project_form.html', {'form': form, 'formset': formset})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})


def custom_login_view(request, *args, **kwargs):
    if request.method == 'POST':
        logger.debug('Tentativa de login para o usuário: %s', request.POST.get('username'))
        
    response = auth_views.LoginView.as_view()(request, *args, **kwargs)
    
    if request.user.is_authenticated:
        logger.debug('Usuário autenticado com sucesso: %s', request.user.username)
    else:
        logger.debug('Falha na autenticação do usuário.')

    return response

@login_required
@require_POST
def update_task_status(request, task_id):
    try:
        task = get_object_or_404(Task, id=task_id, project__owner=request.user)
        data = json.loads(request.body)
        new_status = data.get('status')

        task.status = new_status
        task.save()

        return JsonResponse({'success': True})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
    
@login_required
def create_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', pk=project.id)
    else:
        form = TaskForm()
    return render(request, 'projects/project_detail.html', {'form': form, 'project': project})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id) 
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  
        if form.is_valid(): 

            if not form.cleaned_data.get('due_date'):
                task.due_date = task.due_date 

            form.save()  
            return redirect('project_detail', pk=task.project.id) 
        else:
            print("\n", form.errors)
            return render(request, 'projects/project_detail.html', {'form': form, 'task': task})
    else:
        form = TaskForm(instance=task)
    return render(request, 'projects/project_detail.html', {'form': form, 'task': task})