from django.db import models



class Bills(models.Model):
    quantity: int = models.IntegerField()
    value: int = models.SmallIntegerField()

    def __str__(self):
        return str(self.value)

class Box(models.Model):
    def __str__(self):
        return self.storage
    storage = models.ForeignKey(Bills, on_delete=models.CASCADE)