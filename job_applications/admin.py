from django.contrib import admin
from .models import Application, Job

# Register your models here.
@admin.register(Application)
class ApplicationModelAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'phone', 'resume', 'status', 'applied_date']

@admin.register(Job)
class JobModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'desc', 'dept']