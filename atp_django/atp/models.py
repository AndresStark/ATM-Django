from django.db import models



class Bills(models.Model):
    quantity: int = models.IntegerField()
    value: int = models.SmallIntegerField()

    def __str__(self):
        return str(self.value)


class Request(models.Model):
    request = models.IntegerField(default=0)
    requested_bills = {}
    transaction_text = models.CharField(max_length=100, default="Soy un cajero malo, he sido malo y no puedo darte esa cantidad")

    def __str__(self):
        return ("Se solicitó: " + self.request)


class Transaction(models.Model):
    storage = []
    request = (models.ForeignKey(Request, on_delete=models.DO_NOTHING),)

    def __str__(self):
        return self.storage