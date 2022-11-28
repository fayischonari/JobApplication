from random import choices
from django.db import models

# Create your models here.
class FormDetails(models.Model):
    #choices for the fields
    GENDER = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    JOB = [
        ("React Developer", "React Developer"),
        ("Node.js Developer", "Node.js Developer"),
        ("Vue.js Developer", "Vue.js Developer"),
    ]
    #fields
    EXP = [("0", "Fresher"), ("1", "0-2 years"), ("2", "3-6 years"), ("3", "7+ years")]
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER)
    dob = models.DateField()
    jobrole = models.CharField(max_length=30, choices=JOB)
    experience = models.CharField(max_length=20, choices=EXP)
    linkedin = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name 
