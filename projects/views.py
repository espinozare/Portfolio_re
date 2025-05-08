from django.shortcuts import render, get_object_or_404
from .models import Project
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def projects(request):
    projects = Project.objects.order_by('-created_date')
    paginator = Paginator(projects,2)
   
    data = {
        'projects': projects,
        
        }
    
    return render(request, 'projects/projects.html', data)

def project_detail(request,id):
    single_project=get_object_or_404(Project,pk=id)

    data = {
        'single_project': single_project,
    }

    return render(request,'project/project_detail.html', data)