from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseRedirect
from django.views import generic
from django.views.generic import View

from .forms import NumberForm
from .models import Bills, Request, Transaction


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
        if transaction.transaction_status == "On going":
            return transaction
        else:
            return 0 


class UserFormView(View):
    form_class = NumberForm
    template_name = 'atp/request.html'

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
        

# class RequestView(generic.ListView):
#     template_name: str = 'atp/request.html'
#     context_object_name = 'request_object'

#     def get_queryset(self):
#         """
#         Returns the amount of every bill for the amount requested if available,
#         if not, it returns a "No Money" message
#         """
#         pass
        
        
        