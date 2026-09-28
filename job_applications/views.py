from django.db import IntegrityError
from django.shortcuts import render, redirect
from . import forms
from .models import Application, Job

# Create your views here.
def home(req):
    return render(req, 'home.html')

def job(req):
    jobs = Job.objects.all()
    return render(req, 'job.html', {'jobs': jobs})

def form(req, id):
    if req.method == 'POST':
        data = req.POST
        resume = req.FILES.get('resume')
        try:
            Application.objects.create(name= data.get('name'), email= data.get('email'), phone= data.get('phone'), resume= resume, job_id=id)
            return redirect('success')
        except IntegrityError:
            print('duplicate...')
            return render(req, 'form.html', {'already_exist': 'You have already applied for this job...Thankyou'})
    else:
        return render(req, 'form.html', {'form': forms.ApplicationForm, 'id': id})

def success(req):
    return render(req, 'success.html')