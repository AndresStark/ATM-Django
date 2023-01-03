from django.contrib import admin
from .models import Bills, Request, Transaction

admin.site.register(Request)
admin.site.register(Bills)
admin.site.register(Transaction)
