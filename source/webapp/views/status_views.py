from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.db.models import ProtectedError
from webapp.models import Status
from webapp.forms import StatusForm
from .base_views import ListView


class StatusIndexView(ListView):
    context_key = 'statuses'
    model = Status
    template_name = 'status/status_index.html'


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'status/status_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            Status.objects.create(
                status_name=form.cleaned_data['status_name'],
            )
            return redirect('status_index',)
        else:
            return render(request, 'status/status_create.html', context={'form': form})


class StatusUpdateView(View):
    def get(self, request, pk):
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data={
            'status_name': status.status_name
        })
        return render(request, 'status/status_update.html', context={'form': form, 'status':status})

    def post(self, request, pk):
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.status_name=form.cleaned_data['status_name']
            status.save()
            return redirect('status_index')
        else:
            return render(request, 'status/status_update.html', context={'form': form, 'status':status})


class StatusDeleteView(View):
    def get(self, request, pk):
        status = get_object_or_404(Status, pk=pk)
        return render(request, 'status/status_delete.html', context={'status': status})

    def post(self, request, pk):
        status = get_object_or_404(Status, pk=pk)
        try:
            status.delete()
            return redirect('status_index')
        except ProtectedError:
            return render(request, 'error.html')

