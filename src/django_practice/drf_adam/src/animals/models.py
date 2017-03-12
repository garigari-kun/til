from django.db import models

class Kitten(models.Model):
    name = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    age = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name)


class Puppy(models.Model):
    name = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    age = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name)
