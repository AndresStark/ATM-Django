from django import forms
from .models import Bills, Transaction

class NumberForm(forms.Form):
    digital_number = forms.IntegerField()