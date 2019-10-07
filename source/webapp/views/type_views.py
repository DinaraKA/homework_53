from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView
from django.db.models import ProtectedError
from webapp.models import Type
from webapp.forms import TypeForm
from .base_views import UpdateView


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


class TypeDeleteView(View):
    def get(self, request, pk):
        type = get_object_or_404(Type, pk=pk)
        return render(request, 'type/type_delete.html', context={'type':type})

    def post(self, request, pk):
        type = get_object_or_404(Type, pk=pk)
        try:
            type.delete()
            return redirect('type_index')
        except ProtectedError:
            return render(request, 'error.html')


