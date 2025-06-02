from django.core.exceptions import ValidationError
from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    # def clean(self):
    #     if Employee.objects.filter(email=self.email).exclude(id=self.id).exists():
    #         raise ValidationError("Email must be unique.")
    #     if Employee.objects.filter(phone=self.phone).exclude(id=self.id).exists():
    #         raise ValidationError("Phone must be unique.")

    # def save(self, *args, **kwargs):
    #     self.full_clean() 
    #     super().save(*args, **kwargs)
