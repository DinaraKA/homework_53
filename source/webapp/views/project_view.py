from django.core.paginator import Paginator
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from webapp.forms import ProjectTaskForm, ProjectForm
from webapp.models import Project

class ProjectIndexView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project/project_index.html'
    ordering = ['created_at']
    paginate_by = 5
    paginate_orphans = 1


class ProjectView(DetailView):
    context_object_name = 'project'
    model = Project
    pk_url_kwarg = 'pk'
    template_name = 'project/project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectTaskForm()
        projects = context['project'].projects.order_by('-created_at')
        self.paginate_tasks_to_context(projects, context)
        return context

    def paginate_tasks_to_context(self, tasks, context):
        paginator = Paginator(tasks, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['tasks'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project/project-create.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_index')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})
