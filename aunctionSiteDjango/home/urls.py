from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product-form/', views.product_form, name='product-form'),

]