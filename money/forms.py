from django import forms


class CurrencyForm(forms.Form):
    currency = forms.CharField(help_text="Выберете валюту из которой хотите конвертировать: Например USD или EUR")
    currency1 = forms.CharField(help_text="Выберете валюту в которою хотите конвертировать: Например USD или EUR")
    number = forms.FloatField(help_text="Выберете сумму для конвертации: Например 2 или 3")
