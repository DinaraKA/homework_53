from django.urls import reverse
from django.views.generic import ListView, CreateView
from webapp.models import Type
from webapp.forms import TypeForm
from .base_views import UpdateView, DeleteExceptionView


class TypeIndexView(ListView):
    context_object_name = 'types'
    model = Type
    template_name = 'type/type_index.html'


class TypeCreateView(CreateView):
    model = Type
    template_name = 'type/type_create.html'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('type_index')


class TypeUpdateView(UpdateView):
    model = Type
    template_name = 'type/type_update.html'
    form_class = TypeForm

    def get_redirect_url(self):
        return reverse('type_index')


class TypeDeleteView(DeleteExceptionView):
    context_key = 'type'
    template_name = 'type/type_delete.html'
    model = Type

    def get_redirect_url(self):
        return reverse('type_index')

