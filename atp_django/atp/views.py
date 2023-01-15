from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseRedirect
from django.views import generic
from django.views.generic import View

import math

from .forms import NumberForm
from .models import Bills, Transaction


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# class IndexView(generic.ListView):
#     template_name: str = 'atp/index.html'
#     context_object_name = "monetary_state"

#     def get_queryset(self):
#         """
#         Waits for request
#         """
        # def number_changing(id, num):
        #     n = Request.objects.get(id=id)
        #     n.requested_amount = int(str(n.requested_amount) + str(num))            
        # return Request.objects.get(id=1)



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
    template_name = 'atp/request.html'

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
    context_object_name = "money"

    def get_queryset(self):
        """
        Regresa una imagen de cada billete solicitado si está disponible,
        Si no lo está, retorna un mensaje "No hay dinero"
        """
        box = Bills.objects.all()
        money = int(NumberForm.digital_number)
        bills_requested = []
        papers = 0
        # transaction = Transaction.objects.get(id=1)

        bill_1 = Bills()
        bill_1.value = 1
        bill_1.quantity = 5

        bill_2 = Bills()
        bill_2.value = 5
        bill_2.quantity = 7

        bills_requested.append(bill_1)
        bills_requested.append(bill_2)


        for bi in box:
            if money > 0:
                div = math.floor(money / bi.value)
                if div > bi.quantity:
                    papers = bi.quantity
                else:
                    papers = div
                
                
                bills_requested.append(Bills())
                money -= bi.value * papers
                if money <= 0:
                    bi.quantity -= papers
        
        n = []
        total_t = Transaction.objects.all()
        for i in total_t:
            n.append(i.pk)
        
        return Transaction.objects.get(pk=max(n))
        
        # if money > 0:
        #     transaction.message = "Soy un cajero malo, he sido malo y no puedo darte esa cantidad"
        # else:
        #     for i in bills_requested:
        #         if i.quantity > 0:
        #             transaction.message = "Todo está OK"
        #             for e in i.quantity:
        #                 i.show()

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                n = []
                total_t = Transaction.objects.all()
                for i in total_t:
                    n.append(i.pk)
                t = Transaction.objects.get(pk=max(n))
                t.status = "Finished"
                t.message = "The transaction was done correctly"
                t.save()
                return render(request, 'atp/money.html', {'form': form})
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
                t = Transaction.objects.get(pk=max(n))
                t.status = "Finished"
                t.message = "The transaction was done correctly"
                t.save()
                return render(request, 'atp/money.html', {'form': form})
        else:
            form = self.form_class()

        return render(request, 'atp/money.html', {'form': form})
        
        
        