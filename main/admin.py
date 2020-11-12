from django.contrib import admin
from .models import Solution, Job

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'short_description', 'responsibility_1', 'responsibility_2', 'responsibility_3',
                    'requirement_1', 'requirement_2', 'requirement_3', 'nice_to_have_1', 'nice_to_have_1')
