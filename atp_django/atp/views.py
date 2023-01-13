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
    context_object_name = 'current_number'

    def get_queryset(self):
        """
        Escribe la cantidad de dinero de la transacción que está en proceso,
        o escribe cero para que una nueva transacción sea ejecutada
        """
        transaction = Transaction.objects.get(id=1)
        if transaction.status == "On going":
            return transaction
        else:
            return 0 


class UserFormView(generic.ListView):
    form_class = NumberForm
    template_name = 'atp/request.html'
    context_object_name = 'requests'

    def get_queryset(self):
        """
        Verifica si la cantidad de dinero solicitada puede entregarse según 
        la cantidad de billetes almacenados en la ATP machine
        """
        box = Bills.objects.all()
        money = int(NumberForm.digital_number)
        bills_requested = []
        papers = 0
        # transaction = Transaction.objects.get(id=1)

        for bi in box:
            if money > 0:
                div = math.floor(money / bi.value)
                if div > bi.quantity:
                    papers = bi.quantity
                else:
                    papers = div
                
                
                bills_requested.append(Bills(bi.value, papers).save())
                money -= bi.value * papers
                if money <= 0:
                    bi.quantity -= papers
        
        return money
        
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
                return render(request, 'atp/request.html', {'form': form})
        else:
            form = self.form_class()

        return render(request, 'atp/request.html', {'form': form})

    def get(self, request):
        if request.method == 'GET':
            form = self.form_class(request.GET)
            if form.is_valid():
                return render(request, 'atp/request.html', {'form': form})
        else:
            form = self.form_class()

        return render(request, 'atp/request.html', {'form': form})

        

class MoneyView(generic.ListView):
    template_name: str = 'atp/money.html'
    context_object_name = 'requested_money'

    def get_queryset(self):
        """
        Returns the amount of every bill for the amount requested if available,
        if not, it returns a "No Money" message
        """
        pass
        
        
        