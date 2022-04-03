from django.urls import path
from product.views import *
from django.contrib.auth.views import LoginView
from django.contrib import admin

urlpatterns = [
    path('admin',admin.site.urls),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('products', viewproducts, name="products"),
    path('add', createProduct, name="add"),
    path('delete/<int:id>', deleteProduct, name="delete"),
    path('update/<int:id>', update, name="update"),
    path('updateproduct/<int:id>', updateProduct, name="updateProduct"),
    path('create', create, name="create"),
    path('create/cvs', AddProductsCSV, name="csv"),
    path('get/<int:id>',viewproduct ,name='product'),
]
