from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from webapp.models import Task

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context