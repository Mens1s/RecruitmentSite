from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Person(AbstractUser):
    school = models.CharField(max_length=100)
    last_experience = models.CharField(max_length=100)
    is_working = models.BooleanField(default=False)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)

    is_recruiter = models.BooleanField(default=False)
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    # cv = models.FileField(upload_to='user_cv/', null=True, blank=True)


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    creator = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='created_jobs')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    job_nature = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)

    def __str__(self):
        return self.title + self.company
