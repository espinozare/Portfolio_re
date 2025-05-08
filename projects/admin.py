from django.contrib import admin
from .models import Project
from django.utils.html import format_html

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):

    def thumbnail(self,object):
        return format_html('<img src={} width="40" style="border-radius:50px;" />'.format(object.project_photo.url))

    thumbnail.short_description='Project Image'

    list_display=('id','thumbnail','project_name','is_featured',)
    list_display_links=('id','thumbnail','project_name',)

admin.site.register(Project, ProjectAdmin)

