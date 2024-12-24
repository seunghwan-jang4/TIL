from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list_view, name = 'product_list'),
    path('cerate/', views.product_create_view, name = 'produt_create'),
]

