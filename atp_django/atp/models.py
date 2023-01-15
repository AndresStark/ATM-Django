from django.db import models


class Transaction(models.Model):
    amount = models.IntegerField(default=0)
    aux_money = models.IntegerField(default=0)
    status = models.CharField(max_length=100, default="On going")
    message = models.CharField(max_length=100, default="Transacción en proceso")

    def __str__(self):
        return str(self.pk)

        
class Bills(models.Model):
    quantity: int = models.IntegerField()
    value: int = models.SmallIntegerField()
    img = models.CharField(max_length=100, default="atp/images/cajero.gif")

    def __str__(self):
        return str(self.value)