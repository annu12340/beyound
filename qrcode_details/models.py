from django.db import models


class Qrcode_info(models.Model):

    childname = models.CharField(max_length=30)
    relationship = models.CharField(max_length=30)
    streetaddress = models.CharField(max_length=30)
    towncity = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.parentname
