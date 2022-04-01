from django.urls import path
from product.views import *

urlpatterns = [
    path('', login, name="login"),
    path('products', viewproducts, name="products"),
    path('add', createProduct, name="create"),
    path('delete/<int:id>', deleteProduct, name="delete"),
    path('update/<int:id>', update, name="update"),
    path('updateproduct/<int:id>', updateProduct, name="updateProduct"),
    path('create/cvs', AddProductsCSV, name="addcvs"),
    path('get/<int:id>',viewproduct ,name='product'),
]
