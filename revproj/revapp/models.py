from django.db import models

# Create your models here.
class RevModel(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()

def __str__(self):
    return self.name

