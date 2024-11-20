from django.shortcuts import render, redirect
from .forms import JobApplicationForm

def job_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = JobApplicationForm()
    
