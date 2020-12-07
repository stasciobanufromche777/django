from django.http import HttpResponse
from django.shortcuts import render

from money.forms import CurrencyForm


def index(request):
    if request.method == "POST":
        currency = request.POST.get("currency")
        currency1 = request.POST.get("currency1")
        number = request.POST.get("number")

        if currency == "EUR" and currency1 == "USD":
            b = 1.20
            count = float(number) * b
            return HttpResponse(f'"<h2>Конвертация:{count}</h2>"')

        if currency == "USD" and currency1 == "EUR":
            a = 0.8
            count = float(number) * a
            return HttpResponse(f'"<h2>Конвертация:{count}</h2>"')

    else:
        currencyform = CurrencyForm()
        return render(request, "main.html", {"form": currencyform})
