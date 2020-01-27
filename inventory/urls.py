from django.urls import path
from inventory.views import stock_list, create_product, create_client

urlpatterns =[
    path('',stock_list,name='stock_list'),
    path('createproduct/', create_product, name='create_product'),
    path('createclient/', create_client, name='create_client'),
]