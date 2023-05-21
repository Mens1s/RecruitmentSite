from django.db import models

# Create your models here.
class Applications(models.Model):
    job_id = models.CharField(max_length=100)
    applicant_username = models.CharField(max_length=100)
