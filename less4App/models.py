from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Employee Name", max_length=100)
    email = models.EmailField("Email Address", max_length=100)
    dob = models.DateTimeField("Date of Birth")
    salary = models.FloatField("Basic Salary")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employees"
