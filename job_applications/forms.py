from django import forms
from .models import Application, Job

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'phone', 'resume']