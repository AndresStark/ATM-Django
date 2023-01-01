from django.contrib import admin
from .models import Bills, Box, Request

admin.site.register(Request)
admin.site.register(Bills)
admin.site.register(Box)
