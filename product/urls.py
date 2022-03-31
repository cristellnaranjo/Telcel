from django.urls import path
from product.views import *

urlpatterns = [
    # path('', viewproducts, name="products"),
    path('products', viewproducts, name="products"),
    path('create', createProduct, name="create"),
    path('delete/<int:id>', deleteProduct, name="delete"),
    path('update', updateProduct, name="update"),
    path('create/cvs', AddProductsCSV, name="addcvs"),
    path('get/<int:id>',viewproduct ,name='product'),
]
