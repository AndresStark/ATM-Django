from django.db import models


class Transaction(models.Model):
    amount = models.IntegerField(default=0)
    status = models.CharField(max_length=100, default="Good")
    message = models.CharField(max_length=100, default="Todo está OK")
    requested_bills = []

    def __str__(self):
        return str(self.amount)

        
class Bills(models.Model):
    quantity: int = models.IntegerField()
    value: int = models.SmallIntegerField()
    url = models.URLField(max_length=200, default="")
    family = models.IntegerField(default=0)

    def __str__(self):
        return str(self.value)