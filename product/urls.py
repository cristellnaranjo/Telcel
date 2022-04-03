from django.urls import path
from product.views import *

urlpatterns = [
    path('', login, name="login"),
    path('products', viewproducts, name="products"),
    path('add', createProduct, name="add"),
    path('delete/<int:id>', deleteProduct, name="delete"),
    path('update/<int:id>', update, name="update"),
    path('updateproduct/<int:id>', updateProduct, name="updateProduct"),
    path('create', create, name="create"),
    path('create/cvs', AddProductsCSV, name="csv"),
    path('get/<int:id>',viewproduct ,name='product'),
]
