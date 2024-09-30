from django.db import models

# Create your models here.

job_type=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class job(models.Model):
    title=models.CharField(max_length=100)
    #location
    job_type=models.CharField(max_length=15, choices=job_type)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    #category
    experience=models.IntegerField(default=1)

    def __str__(self):
        return self.title
