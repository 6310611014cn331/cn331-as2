from django.db import models
from subject.models import quotas
from django.contrib.auth.models import User

# Create your models here.
class user_quotas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , related_name="usequota")
    subject = models.ManyToManyField(quotas, blank=True, related_name="user_quota")
    amount_taken = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user}"