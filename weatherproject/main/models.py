from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Graphic(models.Model):
    name = models.CharField(max_length=30),
    text=models.TextField(max_length=250)

    def __str__(self):
        return self.name
