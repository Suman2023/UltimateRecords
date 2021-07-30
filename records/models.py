from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class User(models.Model):
    name = models.TextField(max_length=40, blank=False)
    age = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(100)])
    email = models.EmailField(max_length=254, blank=False)
    phone = models.IntegerField(validators=[MinValueValidator(10000000000)],
                                blank=False)
    image = models.ImageField(upload_to='upload/',
                              height_field=None,
                              width_field=None,
                              max_length=None)
    first_meeting = models.TextField(blank=False)
    friendship = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)], blank=False)
    choices = models.TextField(blank=False)
    any_plans = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Plan(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    plans = models.TextField()
    datetime = models.DateTimeField()

    def __str__(self):
        return self.plans
