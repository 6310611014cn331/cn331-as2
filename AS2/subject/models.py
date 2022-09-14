from django.db import models

# Create your models here.

# class list_student(models.Model):
#     student_name = models.CharField(max_length=64)
#     student_id = models.CharField(max_length=10)


class detail(models.Model):
    # origin = models.ForeignKey(list_student, on_delete=models.CASCADE)
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=64)
    section = models.CharField(max_length=4, null=True)
    semester = models.CharField(max_length=4, null=True)
    year = models.CharField(max_length=4, null=True)


    def __str__(self):
        return f"{self.code} {self.name} "

class quotas(models.Model):
    sit = models.IntegerField()
    details = models.ManyToManyField(detail, blank=True, related_name="qouta")
    
    def __str__(self):
        return f"{self.sit}"
    