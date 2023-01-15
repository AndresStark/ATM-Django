from django.db import models


class Transaction(models.Model):
    amount = models.IntegerField(default=0)
    status = models.CharField(max_length=100, default="On going")
    message = models.CharField(max_length=100, default="Transacción en proceso")
    requested_bills = []

    def __str__(self):
        return str(self.pk)

        
class Bills(models.Model):
    quantity: int = models.IntegerField()
    value: int = models.SmallIntegerField()
    url = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.value)