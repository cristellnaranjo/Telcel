from django.contrib import admin
from django.urls import include, path
from product.views import *


urlpatterns = [
    path('', include('product.urls'))
]
