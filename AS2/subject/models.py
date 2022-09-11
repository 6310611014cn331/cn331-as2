from django.db import models

# Create your models here.
class detial(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"