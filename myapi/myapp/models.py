from django.db import models

# Create your models here
class todo(models.Model):
    title=models.CharField(max_length=100)
    task=models.CharField(max_length=100)
    date=models.DateTimeField()

    def __str__(self):
        return self.title