from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import generic

from .models import Bills, Request, Transaction


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(generic.ListView):
    template_name: str = 'atp/index.html'
    context_object_name = "monetary_state"

    def get_queryset(self):
        """
        Waits for request
        """
        request_screen = 0

        cajita = Bills.objects.all()
        return cajita, request_screen
        # Request(id=1, request=HttpRequest.getvalue()).save()
        

class RequestView(generic.ListView):
    template_name: str = 'atp/request.html'
    def get_queryset(self):
        """
        Returns the amount of every bill for the amount requested if available,
        if not, it returns a "No Money" message
        """
        pass