from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import generic


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(generic.ListView):
    template_name: str = 'atp/index.html'
    def get_queryset(self):
        pass
    

    def request():
        """
        Stores the amount of money requested
        """

class RequestView(generic.ListView):
    template_name: str = 'atp/request.html'
    def get_queryset(self):
        pass

    def transaction():
        """
        Returns the amount of every bill for the amount requested if available,
        if not, it returns a "No Money" message
        """
        quantity = HttpRequest.getvalue(self=HttpRequest)