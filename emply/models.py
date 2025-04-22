from django.db import models

# Create your models here.


class Employe(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)
    dob = models.DateField()
    allocated_salary = models.DecimalField(max_digits=10, decimal_places=2)
    current_salary = models.DecimalField(max_digits=10, decimal_places=2)
    leave_taken = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
