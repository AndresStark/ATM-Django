from django.urls import path
from . import views

app_name = "atp"
urlpatterns = [
    # ex: /atp/
    path("", views.IndexView.as_view(), name="index"),
    path("request/", views.RequestView.as_view(), name="request"),
]