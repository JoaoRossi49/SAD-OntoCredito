from django.urls import path
from .views import *


urlpatterns = [
    path('clientes/', ClienteList.as_view())]
