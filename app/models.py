from django.db import models

# Create your models here.
class Customer(models.Model):
    Username= models.CharField(max_length=300, null=True)
    password = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.Username