from django.db import models

class JobApplication(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    post = models.CharField(max_length=100)
    email = models.EmailField()
    qualification = models.TextField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name
