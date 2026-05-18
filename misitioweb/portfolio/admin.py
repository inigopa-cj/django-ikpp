from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ('title', 'created')
    ordering = ('title', 'created')
    search_fields = ('title', 'description')
    date_hierarchy = 'created'

admin.site.register(Project, ProjectAdmin)