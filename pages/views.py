from django.shortcuts import render
from projects.models import Project

# Create your views here.
def home(request):
    featured_projects=Project.objects.order_by('-created_date').filter(is_featured=True)
    data={
        'featured_projects':featured_projects,
    }
    return render(request, 'pages/home.html', data)
