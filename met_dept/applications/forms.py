from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'dob', 'age', 'post', 'email', 'qualification', 'resume']
