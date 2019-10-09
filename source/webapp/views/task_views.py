from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from webapp.models import Task
from webapp.forms import TaskForm


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
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'task/delete.html'
    success_url = reverse_lazy('index')



