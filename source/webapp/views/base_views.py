from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404


class ListView(TemplateView):
    context_key = 'objects'
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.get_oblects()
        return context

    def get_oblects(self):
        return self.model.objects.all()


class DetailView(TemplateView):
    context_key = 'object'
    model = None
    key_kwargs = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = get_object_or_404(self.model, pk=self.kwargs.get(self.key_kwargs))
        return context



