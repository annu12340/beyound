from django.db import models


class Authorities(models.Model):
    name = models.CharField(max_length=30)
    contact_number = models.IntegerField()

    def __str__(self):
        return self.name


class Neighbours(models.Model):
    name = models.CharField(max_length=30)
    contact_number = models.IntegerField()

    def __str__(self):
        return self.name


class Friends(models.Model):
    name = models.CharField(max_length=30)
    contact_number = models.IntegerField()

    def __str__(self):
        return self.name
