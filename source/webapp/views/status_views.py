from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.db.models import ProtectedError
from webapp.models import Status
from webapp.forms import StatusForm
from webapp.views.base_views import CreateView


class StatusIndexView(ListView):
    context_object_name = 'statuses'
    model = Status
    template_name = 'status/status_index.html'


class StatusCreateView(CreateView):
    model = Status
    template_name = 'status/status_create.html'
    form_class = StatusForm

    def get_redirect_url(self):
        return reverse('status_index')


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

