from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Person(models.Model):
    name = models.TextField(max_length=40, blank=False, unique=True)
    age = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(100)])
    email = models.EmailField(max_length=254, blank=False)
    phone = models.IntegerField(null=True)
    image = models.ImageField(upload_to='upload/', )
    first_meeting = models.TextField(blank=False)
    friendship = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)], blank=False)
    choices = models.TextField(blank=False)
    any_plans = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Plan(models.Model):
    profile = models.ForeignKey(Person, on_delete=models.CASCADE)
    plans = models.TextField()
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.plans
