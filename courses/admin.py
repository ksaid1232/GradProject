from typing import Any
from django.contrib import admin
from .models import Course , Instructor , Customer ,Section
from django import forms
from django_api_admin.sites import site


# Register your models here.
def get_duration(video):
    return 1

class SectionInline(admin.TabularInline):
    model = Section
    fields = ["title", 'description','video_File','duration']
    readonly_fields = ['duration']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    
    list_display = ['name','is_popular','is_trending','description','image','rating','number_of_hours','price']
    fields = ["name", 'is_popular','is_trending','description','image','rating','instructor','number_of_hours','price']
    readonly_fields=['number_of_hours']
    inlines = [SectionInline]

    def save_related(self, request: Any, form: Any, formsets: Any, change: Any) -> None:
        total_hours = 0
        for formset in formsets:
            instances = formset.save(commit=False)
            
            for instance in instances:
                instance.duration = get_duration(instance.video_File)
                total_hours+=instance.duration
        form.instance.number_of_hours = total_hours
        form.save()
        return super().save_related(request, form, formsets, change)
    

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'rating')
    fields = ('first_name', 'last_name', 'rating')



admin.site.register(Section)
site.register(Section)