from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from webapp.models import Task
from webapp.forms import TaskForm
from .base_views import UpdateView


class IndexView(ListView):
    context_object_name = 'tasks'
    model = Task
    template_name = 'task/index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class TaskView(DetailView):
    context_object_name = 'task'
    model = Task
    pk_url_kwarg = 'pk'
    template_name = 'task/task.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task/create.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/update.html'
    form_class = TaskForm

    def get_redirect_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task/delete.html', context={'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')


