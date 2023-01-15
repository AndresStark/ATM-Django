from django import forms
from django.db import models
from .models import Bills, Transaction

class NumberForm(forms.Form):
    digital_number = forms.IntegerField()

    def __str__(self):
        return str(self.digital_number)