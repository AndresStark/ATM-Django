from django.urls import path
from . import views, forms

app_name = "atp"
urlpatterns = [
    # ex: /atp/
    path("", views.IndexView.as_view(), name="index"),
    path("request/", views.UserFormView.as_view(), name="request"),
]