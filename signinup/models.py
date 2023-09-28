from django.db import models
from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
# MATERIAL_CHOICES = (
#     ('Note Book', 'Note Book'),
#     ('Pen', 'Pen'),
# )
PURPOSE_CHOICES = (
    ('Enquiry', 'Enquiry'),
    ('Place Order', 'Place Order'),
    ('Return', 'Return'),
)
# Create your models here.
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        # managed = True
        db_table = 'myapp_department'


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        # managed = True
        db_table = 'myapp_course'


class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number =models.PositiveBigIntegerField()
    email_id = models.EmailField(max_length=200)
    address = models.TextField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    purpose = models.CharField(max_length=12, choices=PURPOSE_CHOICES)
    material = models.CharField(max_length=13)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'myapp_std'
