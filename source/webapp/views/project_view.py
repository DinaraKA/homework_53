from django.views.generic import ListView
from webapp.models import Project

class ProjectIndexView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project/project_index.html'
    ordering = ['created_at']
    paginate_by = 5
    paginate_orphans = 1