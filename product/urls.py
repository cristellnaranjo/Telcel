from django.urls import path
from product.views import *
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib import admin

urlpatterns = [
    path('',redirec, name="redirect"),
    path('admin',admin.site.urls),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('products', viewproducts, name="products"),
    path('add', createProduct, name="add"),
    path('delete/<int:id>', deleteProduct, name="delete"),
    path('update/<int:id>', update, name="update"),
    path('updateproduct/<int:id>', updateProduct, name="updateProduct"),
    path('create', create, name="create"),
    path('create/csv', AddProductsCSV, name="csv"),
    path('get/<int:id>',viewproduct ,name='product'),
    path('logout',logoutview ,name='logout'),
    path('password_reset', PasswordResetView.as_view(template_name='password_reset_form.html', html_email_template_name='password_reset_email.html'), name='password_reset'),
    path('password_reset_done',PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('P<uidb64>[0-9A-Za-z\-]'+'/P<token>'+'/',PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('prueba',prueba ,name='prueba'),
    path('prestashop/products', viewproductsPrestashop, name="products_Presta"),
    path('prestashop/get/<int:id>',viewproductPrestashop ,name='product_Presta'),
    path('prestashop/delete/<int:id>', deleteProductPrestashop, name="delete_Presta"),
    # path('prestashop/update/<int:id>', update, name="update"),
    # path('prestashop/updateproduct/<int:id>', updateProduct, name="updateProduct"),
    # path('prestashop/create', create, name="create"),
]
