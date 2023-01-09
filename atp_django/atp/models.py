from django.db import models



class Bills(models.Model):
    quantity: int = models.IntegerField()
    value: int = models.SmallIntegerField()

    def __str__(self):
        return str(self.value)


class Request(models.Model):
    requested_amount = models.IntegerField(default=0)
    request_status = models.CharField(max_length=100, default="Good")

    def __str__(self):
        return ("Se solicitó: " + str(self.requested_amount))

    def delete(self, current):
        Request.objects.get(id=current).requested_amount=0


class Transaction(models.Model):
    transaction_amount = models.IntegerField(default=0)
    transaction_status = models.CharField(max_length=100, default="Soy un cajero malo, he sido malo y no puedo darte esa cantidad")
    requested_bills = {}
    request = (models.ForeignKey(Request, on_delete=models.DO_NOTHING),)

    def __str__(self):
        return str(self.transaction_amount)