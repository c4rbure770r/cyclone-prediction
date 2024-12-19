from django.db import models

class Alert(models.Model):
    region = models.CharField(max_length=100)
    alert_type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.region} - {self.alert_type}"
