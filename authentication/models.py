# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
class SignupUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    buildingname = models.CharField(max_length=100)
    ROLE_CHOICES = [
        ('watchman', 'Watchman'),
        ('member', 'Member'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='watchman')
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'signup'

    def __str__(self):
        return self.name
    
class AddGuests(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    vehical = models.CharField(max_length=20)
    purpose = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image_path/', null = True, blank = True)

    intime = models.DateTimeField(blank=True, null=True)

    outtime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"