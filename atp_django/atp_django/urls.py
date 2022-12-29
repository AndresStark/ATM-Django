from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('atp/', include("atp.urls")),
    path('admin/', admin.site.urls),
]
