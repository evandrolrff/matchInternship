from django.db import models

class Profile(models.Model):
    communication = models.BooleanField(default=False)
    proactivity = models.BooleanField(default=False)
    organized = models.BooleanField(default=False) # detailed, concerned, very conservative
    planner = models.BooleanField(default=False)
    meticulous = models.BooleanField(default=False)
    responsible = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Person(Profile):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    date = models.DateField()

class Professor(models.Model):
    occupation = models.CharField(max_length=20)
    discipline = models.CharField(max_length=30)
    person = models.ForeignKey(
        'Person', 
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        )
    registration = models.CharField(max_length=25)
    # password

class Student(models.Model):
    field = models.CharField(max_length=20)
    person = models.ForeignKey(
        'Person', 
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        )
    registration = models.CharField(max_length=25)
    semester = models.SmallIntegerField()

class Partner(models.Model):
    name = models.CharField(max_length=25)
    local = models.CharField(max_length=25)

class JobOpportunity(Profile):
    description = models.CharField(max_length=255)
    field = models.CharField(max_length=20)
    number = models.IntegerField()
    workload = models.IntegerField()
    partner = models.ForeignKey(
        'Partner', 
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        )