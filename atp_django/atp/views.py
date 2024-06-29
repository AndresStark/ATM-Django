from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseRedirect
from django.views import generic
from django.views.generic import View

import math

from .forms import NumberForm
from .models import Bills, Transaction



class IndexView(generic.ListView):
    template_name: str = 'atp/index.html'
    context_object_name = 'transaction'

    def get_queryset(self):
        """
        Escribe la cantidad de dinero de la transacción que está en proceso,
        o escribe cero para que una nueva transacción sea ejecutada
        """
        n = []
        total_t = Transaction.objects.all()
        for i in total_t:
            n.append(i.pk)
        t_id = max(n)
        if Transaction.objects.get(pk=t_id).status == "On going":
            transaction = Transaction.objects.get(pk=t_id)
        else:
            transaction = Transaction()
            transaction.save()

        return transaction


class UserFormView(generic.ListView):
    model = Transaction
    form_class = NumberForm
    template_name: str = 'atp/request.html'

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)            
            if form.is_valid():
                n = []
                total_t = Transaction.objects.all()
                for i in total_t:
                    n.append(i.pk)
                t = Transaction.objects.get(pk=max(n))
                t.amount = form.cleaned_data['digital_number']
                t.save()
                return render(request, 'atp/request.html', {'form': form})
        else:
            form = self.form_class()

        return render(request, 'atp/request.html', {'form': form})

    def get(self, request):
        if request.method == 'GET':
            form = self.form_class(request.GET)
            if form.is_valid():
                n = []
                total_t = Transaction.objects.all()
                for i in total_t:
                    n.append(i.pk)
                t = Transaction.objects.get(pk=max(n))
                t.amount = form.cleaned_data['digital_number']
                t.save()
                return render(request, 'atp/request.html', {'form': form})
        else:
            form = self.form_class()

        return render(request, 'atp/request.html', {'form': form})

        

class MoneyView(generic.ListView):
    model = Transaction
    form_class = NumberForm
    template_name: str = 'atp/money.html'


    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                n = []
                total_t = Transaction.objects.all()
                for i in total_t:
                    n.append(i.pk)
                transaction = Transaction.objects.get(pk=max(n))
                
                transaction.requested_bills = []
                box = Bills.objects.all()
                transaction.aux_money = int(form.cleaned_data['digital_number'])
                papers = 0

                for bi in box[::-1]:
                    if transaction.aux_money > 0:
                        div = math.floor(transaction.aux_money / bi.value)
                        if div > bi.quantity:
                            papers = bi.quantity
                        else:
                            papers = div
                        
                        bill = Bills()
                        bill.quantity = papers
                        bill.value = bi.value
                        bill.img = f"atp/images/{bill.value}.jpg"
                        transaction.requested_bills.append(bill)

                        transaction.aux_money -= bi.value * papers
                        if transaction.aux_money > 0:
                            pass
                        else:
                            bi.quantity -= papers

                if transaction.aux_money == 0:
                    transaction.message = "The transaction was done correctly"
                    transaction.status = "Finished"
                    transaction.save()
                else:
                    transaction.message = "Soy un cajero malo, he sido malo y no puedo darte esa cantidad"
                    transaction.status = "Failed"
                    transaction.save()

                return render(request, 'atp/money.html', {'transaction': transaction})
        else:
            form = self.form_class()

        return render(request, 'atp/money.html', {'form': form})

    def get(self, request):
        if request.method == 'GET':
            form = self.form_class(request.GET)
            if form.is_valid():
                n = []
                total_t = Transaction.objects.all()
                for i in total_t:
                    n.append(i.pk)
                transaction = Transaction.objects.get(pk=max(n))
                transaction.status = "Finished"
                transaction.message = "The transaction was done correctly"
                transaction.save()
                return render(request, 'atp/money.html', {'transaction': transaction})
        else:
            form = self.form_class()

        return render(request, 'atp/money.html', {'form': form})
        
        
        