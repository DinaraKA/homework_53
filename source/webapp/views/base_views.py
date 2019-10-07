from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render, redirect


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


class CreateView(View):
    form_class = None
    template_name = None
    model = None
    redirect_url = ''

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, context={'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_redirect_url(self):
        return self.redirect_url

    def form_valid(self, form):
        self.object = self.model.objects.create(**form.cleaned_data)
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form':form})


class UpdateView(View):
    form_class = None
    template_name = None
    model = None
    redirect_url = ''


    def get(self, request, *args, **kwargs):
        object_class = get_object_or_404(self.model, pk=kwargs['pk'])
        form = self.form_class(instance=object_class)
        return render(request, self.template_name, context={'form': form, 'object_class': object_class})

    def post(self, request, *args, **kwargs):
        object_class = get_object_or_404(self.model, pk=kwargs['pk'])
        form = self.form_class(instance = object_class, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_redirect_url(self):
        return self.redirect_url

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form':form})


