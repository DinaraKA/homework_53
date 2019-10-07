from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView
from django.db.models import ProtectedError
from webapp.models import Status
from webapp.forms import StatusForm
from .base_views import UpdateView



class StatusIndexView(ListView):
    context_object_name = 'statuses'
    model = Status
    template_name = 'status/status_index.html'


class StatusCreateView(CreateView):
    model = Status
    template_name = 'status/status_create.html'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_index')


class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'status/status_update.html'
    form_class = StatusForm

    def get_redirect_url(self):
        return reverse('status_index')


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

