from django import forms

class NumberForm(forms.Form):
    digital_number = forms.IntegerField()