from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from webapp.models import Status
from webapp.forms import StatusForm
from .base_views import  DeleteExceptionView



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
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('status_index')


class StatusDeleteView(DeleteExceptionView):
    context_key = 'status'
    template_name = 'status/status_delete.html'
    model = Status

    def get_redirect_url(self):
        return reverse('status_index')
