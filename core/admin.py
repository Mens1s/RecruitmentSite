from django.contrib import admin
from .models import Person, Job, JobCategories

# Register your models here.
admin.site.register(Person)
admin.site.register(Job)
admin.site.register(JobCategories)
