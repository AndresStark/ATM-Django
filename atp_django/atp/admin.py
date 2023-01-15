from django.contrib import admin
from .models import Bills, Transaction

class TransactionAdmin(admin.ModelAdmin):
    fields = ["amount", "aux_money", "status", "message"]

admin.site.register(Bills)
admin.site.register(Transaction, TransactionAdmin)
