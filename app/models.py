from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    given_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    profile_description = models.TextField()
    password = models.CharField(max_length=255)

class Caregiver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    photo = models.BinaryField(null=True)
    gender = models.CharField(max_length=10)
    caregiving_type = models.CharField(max_length=50)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    house_rules = models.TextField()

class Address(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, primary_key=True)
    house_number = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    town = models.CharField(max_length=100)

class Job(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    required_caregiving_type = models.CharField(max_length=50)
    other_requirements = models.TextField()
    date_posted = models.DateField()

class JobApplication(models.Model):
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date_applied = models.DateField()

class Appointment(models.Model):
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    work_hours = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=20, default = "Pending")