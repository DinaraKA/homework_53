from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
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


class TaskCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'task/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type = form.cleaned_data['type']
            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task/create.html', context={'form': form})


class TaskUpdateView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data={
            'summary':task.summary,
            'description':task.description,
            'status':task.status_id,
            'type': task.type_id
        })
        return render(request, 'task/update.html', context={'form': form, 'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary=form.cleaned_data['summary']
            task.description=form.cleaned_data['description']
            task.status=form.cleaned_data['status']
            task.type=form.cleaned_data['type']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task/update.html', context={'form': form, 'task': task})


class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task/delete.html', context={'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')


