from django.db import models



class Bills(models.Model):
    quantity: int = models.IntegerField()
    value: int = models.SmallIntegerField()

    def __str__(self):
        return str(self.value)

class Box(models.Model):
    def __str__(self):
        return self.storage
    storage = []

class Request(models.Model):
    def __str__(self):
        return self.name
    
    request = models.IntegerField(default=0)
    total = models.IntegerField()
    requested_bills = []
    transaction_text = models.CharField(max_length=100, default="Soy un cajero malo, he sido malo y no puedo darte esa cantidad")