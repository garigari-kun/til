from django.db import models


class Person(models.Model):
    SHIRT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length = 100)
    shirt_size = models.CharField(max_length = 1, choices = SHIRT_SIZE)
