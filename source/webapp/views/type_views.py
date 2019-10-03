from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
from django.db.models import ProtectedError
from webapp.models import  Type
from webapp.forms import TypeForm


class TypeIndexView(TemplateView):
    template_name = 'type/type_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'type/type_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            Type.objects.create(
                type_name=form.cleaned_data['type_name'],
            )
            return redirect('type_index',)
        else:
            return render(request, 'type/type_create.html', context={'form': form})


class TypeUpdateView(View):
    def get(self, request, pk):
        type = get_object_or_404(Type, pk=pk)
        form = TypeForm(data={
            'type_name': type.type_name
        })
        return render(request, 'type/type_update.html', context={'form': form, 'type':type})

    def post(self, request, pk):
        type = get_object_or_404(Type, pk=pk)
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.type_name=form.cleaned_data['type_name']
            type.save()
            return redirect('type_index')
        else:
            return render(request, 'type/type_update.html', context={'form': form, 'type':type})


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


