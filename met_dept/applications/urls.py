from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.job_application, name='job_application'),
]
